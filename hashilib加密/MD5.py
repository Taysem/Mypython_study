import  hashlib
usr = input('uername:')
pwd = input('password :')
md5 = hashlib.md5()#创建一个md5 对象
md5.update(bytes(pwd,encoding='utf-8'))#对其进行加密, 需要转换为bytes 类型的
pwd_md5 = md5.hexdigest()#加密的结果
print( pwd_md5 )