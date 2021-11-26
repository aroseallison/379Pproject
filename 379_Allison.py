import socket

# define server and port
host = '0.0.0.0'
port = 9879

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(('', port))
serverSocket.listen(2)
print('Web Server is up on port', port)


while True:
    print('ready to server')
    clientConnection, address = serverSocket.accept()
    try:
        request = clientConnection.recv(1024).decode()
        print(request)
        response = ('HTTP/1.0 200 OK\n\nHello World, You have reached my webpage')
        clientConnection.sendall(response.encode())
        clientConnection.close()
    except IOError:
        print('404 Not Found')
        connection("""HTTP/1.0 404 Not Found\r\n""".encode())
        
serverSocket.close()        
