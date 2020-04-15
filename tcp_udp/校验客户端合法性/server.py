import socket
import hmac
import os

secret_key = b'key'

sk = socket.socket()
sk.bind(('127.0.0.1',6789))
sk.listen()

#对连接的客户端校验时候合法
'''使用hmac  模块校验(内置模块)'''
def check_conn(conn):
	msg = os.urandom(32)
	conn.send(msg)#随发送一个32位的字节数据,加密的bytes
	h = hmac.new(secret_key,msg)
	digest = h.digest()#加密后的digest
	client_digest =conn.recv(1024)#接收client发过来的加密digest
	ret = hmac.compare_digest(digest,client_digest)#对比接收到的client  的和server是否一致
	return ret

conn, addr = sk.accept()
res = check_conn(conn)
if res:
	print('合法的客户端')
	conn.close()
else:
	print('bu合法的客户端')
	conn.close()
sk.close()