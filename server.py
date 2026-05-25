import socket

server=socket.socket()
server.bind(('localhost',5050))
server.listen(5)

print('Server running on port 5050...')

while True:
    client,address=server.accept()

    request=client.recv(4096).decode()

    if 'GET' in request:
        try:
            with open('index.html','r') as f:
                content=f.read()

            response='HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n'+content
        except:
            response='HTTP/1.1 404 Not Found\r\n\r\nFile not found'

    elif 'POST' in request:
        body=request.split('\r\n\r\n',1)[1]

        with open('upload.txt','w') as f:
            f.write(body)

        response='HTTP/1.1 200 OK\r\n\r\nFile Uploaded Successfully'

    else:
        response='HTTP/1.1 400 Bad Request'

    client.send(response.encode())
    client.close()
