import socket

sk =socket.socket()
sk.connect(('127.0.0.1',9876))
# sk.send(b'hhhhhhhhh')
#
# ret = sk.recv(1024)
# print(ret.decode('utf-8'))


while 1:
    msg = input('输入信息为: ')
    sk.send(bytes(msg,encoding='utf-8'))
    if msg =='bye':
        break
    ret = sk.recv(1024).decode('utf-8')
    if ret =='bye':
        sk.send(b'bye')
        break
    print('来自服务端的消息:%s'%ret)

sk.close()

