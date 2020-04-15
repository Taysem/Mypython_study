#client  为发送端
import socket
import os
import json
import struct
# from socket import SOL_SOCKET,SO_REUSEADDR

buffer = 1024

sk = socket.socket()
# sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sk.connect(('127.0.0.1',8001))

# 发送文件
heads={'filename':r'hyd.png',
       'filepath':r'E:\项目',
       'filesize':None}
filepath =os.path.join(heads['filepath'],heads['filename'])
filesize = os.path.getsize(filepath)
# print(os.path.basename(r'F:\my_pythonproject\tcp_udp\基于tcp大文件传输'))
print(filesize)
heads[filesize] = filesize
json_heades = json.dumps(heads)#字典转换为字符串
print(json_heades)
byte_heades = json_heades.encode('utf-8')
print(byte_heades)
# 计算byte_heads长度,方便接收
heades_len = len(byte_heades)#计算报头的长度,方便接收此长度不易粘包
print(heades_len)
pack_len = struct.pack('i',heades_len)#struct  模块将固定转化为4个字节长度
print(pack_len)

#发送,先发报头长度,再发bytes类型报头
sk.send(pack_len)
sk.send(byte_heades)
#在发送文件
with open(filepath,'rb') as f:
    while filesize:
        print(filesize)
        if filesize >= buffer:
            connent = f.read(buffer)#每次读取的大小
            sk.send(connent)
            filesize -= buffer
        else:
            connent = f.read(filesize)
            sk.send(connent)
            break
sk.close()

