# import time
# import sys
# # mq = input('>>>>')
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# # print(getattr(sys.modules['__main__'],'mq')())
# print(getattr(time,'strftime')("%Y-%m-%d %H:%M:%S"))

class Na:
    def __init__(self):
        self.name = 'zhoutaixin'
        self.age = 23
    # def __str__(self):
    #     return '调用的的是方法%s'%self.name
    def __repr__(self):
        return '调用额是%r'%self.age
a = Na()
print(a)