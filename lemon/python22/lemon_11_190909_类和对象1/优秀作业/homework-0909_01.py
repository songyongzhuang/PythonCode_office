# _*_ coding: utf-8 _*_
#@Time    : 2019/9/10 14:18
#@Author  : 满满
#@File    : homework-0909_01.py
#@Email   :867232508@qq.com



'''
1、实现一个手机类，并实例化你的手机。
要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
尽量多的获取不同属性和使用不同的功能。
'''
class Phone():


    def __init__(self,brand,model,price,person):
        self.brand = brand      #品牌
        self.model = model      #型号
        self.price = price      #价格
        self.person = person    #所属人

    ##打电话
    def call(self,called_person):
        str = '{}正在打电话给{}'.format(self.person,called_person)
        return str


    #发短信
    def send_message(self,**args):

        message = {
            'sender': self.person,
            'message': args['message'],
            'recevier': args['recevier']
        }
        str = '''
        ++++++++++++++++++++++++++
        收件人:{recevier}
            {message} 
                   发件人:{sender}
        ++++++++++++++++++++++++++
        '''.format(**message)
        return str


    #拍照
    def photograph(self):
        if self.model in ('智能机','老年机'):
            if self.model == '智能机':
                return '您拍了一张美美的照片'
            else:
                return '不好意思您的手机没有拍照功能'
        return '您的手机型号不明确'


if __name__ == '__main__':
    phone = Phone('华为','智能机',1999,'满满')
    print(phone.photograph())
    print(phone.call('落落'))
    print(phone.send_message(recevier = '落落',message = '我周六想和你去逛街'))


