import socket
from socket import SOL_SOCKET,SO_REUSEADDR

sk = socket.socket()
sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sk.bind(('127.0.0.1',9876))
sk.listen()
conn, addr = sk.accept()
# ret = conn.recv(123)
# print(ret)
# conn.send(bytes('打酱油的是吧',encoding='utf-8'))

while 1:
    ret = conn.recv(123).decode('utf-8')
    print('来自连接方的信息:%s'%ret)
    if ret == 'bye':
        break
    info = input('>>>>>')
    conn.send(bytes(info,encoding='utf-8'))

conn.close()
sk.close()