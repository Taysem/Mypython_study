import socket
import subprocess

sk = socket.socket()
sk.connect(('127.0.0.1',4567))

while 1:
    cmd = sk.recv(1024).decode('gbk')
    if cmd == b'q':
        break
    # cmd = 'ipconfig'
    res = subprocess.Popen(cmd,shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    # print(res.stdout.read().decode('gbk'))
    sk.send(res.stdout.read())
    sk.send(res.stderr.read())

sk.close()