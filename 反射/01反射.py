class A():
    name = 'zhouta'
    @classmethod
    def funca(cls):
        print('i love taylor')

a = A()
# print(a.name)
#hasattr(类名, 方法名)两个参数, 方法在类中则返回true, 不在则返回false
se = hasattr(A,'funca')
print(se)
se2 = hasattr(A,'dd')
print(se2)

se3 = getattr(A,'name')
print(se3)
se4 = getattr(A,'funca')#获取funca内存地址
se4()#执行方法

setattr(A,'age',34)#添加属性age, 添加值为34
print(getattr(A,'age'))  #获取值