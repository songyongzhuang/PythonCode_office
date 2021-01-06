# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : helper.py
# Author       : 大壮
# Create time  : 2019-10-24 20:13
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

import random  # 随机数
import re

from lemon_25_191023_充值接口_用例关联_看这里的.test_practice_01_25.common.config_handler_peizhiwenjian \
    import config  # 读取配置文件
from lemon_25_191023_充值接口_用例关联_看这里的.test_practice_01_25.common.requests_handler_HTTPqingqiu \
    import RequestsHandler  # HTTP请求
from lemon_25_191023_充值接口_用例关联_看这里的.test_practice_01_25.middler_ware.db_handler \
    import MyDBHandler  # 搭桥数据库


def mk_phone():
    """ 随机生成手机号码 """
    phone = '1' + random.choice(['3', '5', '7', '8'])  # 数字随机选择一个
    for i in range(9):  # 取九次
        # 取值九次
        num = str(random.randint(0, 9))  # 随机取整数
        phone += num  # 取一次值在基础上往上加

    return phone


def login():
    """登录，获取 token, member_id"""
    req = RequestsHandler()
    # 登录， 测试账号来登录
    res = req.json('post',
                   # 也可以读取Excel测试数据  采用配置文件，读取配置文件的数据📕
                   config.read('http', 'base_url') + config.read('http', 'login_url'),
                   json={"mobile_phone": config.read('accounts', 'mobile_phone'),
                         "pwd": config.read('accounts', 'password')},
                   headers=eval(config.read('http', 'headers')))
    data = {"token": res['data']['token_info']['token'], "member_id": res['data']['id']}
    return data


class Context:
    """保存临时替换的数据 配置文件读取"""
    phone = config.read('accounts', 'mobile_phone')
    pwd = config.read('accounts', 'password')
    member_id = config.read('accounts', 'member_id')

    @property
    def loan_id(self):
        # Context().loan_id
        """查询数据库，获取最新的 loan.id 作为 Context的 loan_id 属性。"""
        db = MyDBHandler()
        loan = db.query("SELECT * FROM loan ORDER BY id DESC;", one=True)  # 根据 id 降序排列
        return str(loan['id'])

    @property
    def above_balance(self):
        db = MyDBHandler()
        user = db.query('SELECT * FROM member WHERE id=%s;', args=[self.member_id])
        return str(user['leave_amount'] + 1)


def replace_label(target):  # 字符串:replace.
    """用 data 替换 target 里的标签。
    {"mobile_phone":"#phone#", "pwd": "#pwd#"} ==> {"mobile_phone":"137"}
    """
    pattern = r"#(.*?)#"  # 正则表达式
    ctx = Context()
    # 判断是否有符合条件的字符串
    while re.search(pattern, target):
        # 匹配  phone , pwd
        key = re.search(pattern, target).group(1)  # 里面写 1 是因为正则里面有 ( )
        value = getattr(ctx, key, '')
        target = re.sub(pattern, value, target, 1)
    return target


if __name__ == '__main__':
    print(mk_phone())
    print(login())
