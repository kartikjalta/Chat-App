import socket
serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
print(host)
port=10000
serversocket.bind((host,port))
serversocket.listen(5)
msg=[]

while 1:
    
    clientsocket,addr=serversocket.accept()
    #i=input("enter messag to be sent")
    
    while 1:
        msg=clientsocket.recv(1024)
        print(msg)
        i=input("enter messag to be sent")
        clientsocket.send(i.encode('ascii'))
    #clientsocket.send(i.encode('ascii'))
    clientsocket.close()
