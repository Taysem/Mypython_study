import socket
import struct
import json
from socket import SOL_SOCKET,SO_REUSEADDR

buffer = 1024

sk = socket.socket()
sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sk.bind(('127.0.0.1',8001))
sk.listen()
conn, addr = sk.accept()

#server接收端
head_len = conn.recv(4)#报头长度被struct 处理了
head_len = struct.unpack('i',head_len)[0]
json_head = conn.recv(head_len).decode('utf-8')
head = json.loads(json_head)
print(head)
print('sssssssssssssssssssssssssssssssssssssssssssssss')
filesize = head['filesize']
with open(head['filename'],'wb') as f:
    while filesize:
        print(filesize)
        if filesize>= buffer:
            connent = conn.recv(buffer)
            f.write(connent)
            filesize -= buffer
        else:
            connent = conn.recv(filesize)
            f.write(connent)
            break
conn.close()
sk.close()