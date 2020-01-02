# Java  面向对象编程的

# 设计模式  -----接口

# 接口类:  python原生是不支持的

# 抽象类  python 原生支持的

from abc import abstractmethod,ABCMeta

class Payment(metaclass=ABCMeta):
    @abstractmethod
# class Payment():
    def pay(self,money):
        raise NotImplemented #没有实现此方法
    

class Wechat(Payment):
    def pay(self,money):
        print ('微信支付%s' %money)


class Alipay(Payment):
    def pay(self,money):
        print ('支付宝支付%s' %money)


class applePay(Payment):
    def pay(self,money):
        print ('applepay支付%s' % money)

#统一支付接口
def pay(pay_obj,money):
    pay_obj.pay(money)

wechat = Wechat()
alipay = Alipay()
app = applePay()
pay(wechat,100)
pay(app,20)