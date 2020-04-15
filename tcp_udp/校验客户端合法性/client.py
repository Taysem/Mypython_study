import socket
import hmac

secret_key = b'key111'

sk =socket.socket()
sk.connect(('127.0.0.1',6789))

msg = sk.recv(1024)
h = hmac.new(secret_key,msg)
digest = h.digest()
sk.send(digest)

sk.close()