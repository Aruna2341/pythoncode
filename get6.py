import socket

s=socket.socket()
print("socket successfully created")
port=2357
s.bind(('', port))
print("socket binded to %s" %(port))
s.listen(5)
print("socket is listening")
while True:
    c, addr = s.accept()
    print('got connection from', addr)
    c.send(b'thank you for connecting')
    c.close()