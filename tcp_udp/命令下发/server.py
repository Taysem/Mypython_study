import socket

sk = socket.socket()
sk.bind(('127.0.0.1',4567))
sk.listen()

conn, addr = sk.accept()

while 1:
    cmd = input('please input your cmd:')
    if cmd=='q':
        conn.send(b'q')
        break
    conn.send(cmd.encode('gbk'))
    ret =conn.recv(1024).decode('gbk')
    print(ret)
conn.close()
sk.close()
