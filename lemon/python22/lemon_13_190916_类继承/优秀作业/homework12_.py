# 第一题
class Mobile:
    brand = 'unknown'
    type = 'unknown'

    def __init__(self, brand, type, **kwargs):
        self.brand = brand
        self.type = type
        self.phone_no = kwargs.get('phone_no', '-')
        self.os = kwargs.get('os', 'unknown')

    def dial(self, to):
        print('拨打电话{}'.format(to))

    def message(self, to, message):
        print('发短信给：{}， 内容：{}'.format(to, message))

    def get_brand(self):
        return self.brand

    def __repr__(self):
        return f'<Mobile {self.brand}/{self.type}, number:{self.phone_no}>'


class IntelligenceMobile(Mobile):
    '''
    智能手机拨打电话录音
    '''

    def dial(self, to, is_record):
        super().dial(to)
        if is_record:
            print('开始录音')


class AppleMobile(Mobile, IntelligenceMobile):

    '''
    苹果手机拨打电话
    '''
    def dial(self, to, is_record, is_facetime):
        super().dial(to, is_record)
        if is_facetime:
            print('facetime模式开启')


# new_mobile = Mobile('apple', 'iphone xs max', phone_no='13800138000')
# print(new_mobile)
# print(new_mobile.get_brand())
# new_mobile.dial('10086')
# new_mobile.message('10086', '查询套餐余量')


# 第二题
class ExcelManual():

    # 初始化excel名称和sheet表单名称
    def __init__(self, excel_name):
        self._excel = open(excel_name)
        self.sheets: dict = self._excel.get_sheets()

    # 获取sheet表单
    def get_sheet(self, sheet_name):
        return self.sheets.get(sheet_name)

    # 读取单元格
    def read_excel_cell(self, sheet_name, cell_name):
        sh = self.get_sheet(sheet_name)
        if sh is None:
            return None
        return sh.get(cell_name)

    # 修改单元格
    def modify_excel_cell(self, sheet_name, cell_name, value):
        sh = self.get_sheet(sheet_name)
        sh[cell_name] = value


# 第三题
# 定义工具类
class Tool(object):

    def __init__(self, name, description='', price=0):
        '''
        初始化工具信息
        '''
        self.name = name
        self.description = description
        self.price = price


class ToolBox(object):

    def __init__(self):
        """
        初始化工具箱列表
        """
        self._tools = []

    def add_tool(self, tool: Tool):
        '''
        添加工具
        :param tool:
        :return:
        '''
        self._tools.append(tool)

    def delete_tool(self, name):
        '''
        删除工具
        :param name:
        :return:
        '''
        for item in self._tools[::]:
            if item.name == name:
                self._tools.remove(item)

    def get_tool_info(self, name):
        '''
        获取工具的描述信息
        :param name:
        :return:
        '''
        for item in self._tools:
            if item.name == name:
                return item.description

    def __len__(self):
        '''
        获取工具箱中工具总数
        :return:
        '''
        return len(self._tools)

    get_too_total_number = length = __len__
