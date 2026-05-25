# 5a Create Socket for HTTP for Webpage Upload and Download

## AIM
To write a Python program for socket communication using HTTP protocol for webpage upload and download.

## ALGORITHM
1. Start the server.
2. Create socket using Python socket module.
3. Bind server to localhost and port 5050.
4. Listen for incoming requests.
5. Create client socket.
6. Send GET request for webpage download.
7. Send POST request for webpage upload.
8. Process request and send response.
9. Display result.
10. Stop program.

---

## SERVER PROGRAM (server.py)

```python
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
```

---

## CLIENT PROGRAM (client.py)

```python
import socket

client=socket.socket()
client.connect(('localhost',5050))

print('1.Download Webpage')
print('2.Upload Content')

choice=input('Enter your choice: ')

if choice=='1':
 request='GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'

else:
 data=input('Enter text to upload: ')
 request=('POST / HTTP/1.1\r\nHost: localhost\r\nContent-Type:text/plain\r\n\r\n'+data)

client.send(request.encode())
print(client.recv(4096).decode())
client.close()
```

---

## HTML WEBPAGE (index.html)

```html
<!DOCTYPE html>
<html>
<head>
<title>Socket HTTP Demo</title>
</head>
<body>
<h1>HTTP Webpage Upload and Download</h1>
<p>This webpage is served using Python socket programming.</p>
</body>
</html>
```

---

## EXECUTION

```bash
python server.py
python client.py
```

## OUTPUT

### Download
Client → GET request

Server → Returns HTML page

`server`

<img width="730" height="92" alt="image" src="https://github.com/user-attachments/assets/151776ae-9bdd-4722-87ec-d01b39bfdab7" />

`client`

<img width="740" height="412" alt="image" src="https://github.com/user-attachments/assets/cdf352b1-e490-452c-ad01-295fe091e423" />


### Upload
Client → POST request

Server → Saves uploaded text into upload.txt

`server`

<img width="749" height="103" alt="image" src="https://github.com/user-attachments/assets/42ce3726-7be7-4259-b209-e464c8eb4f7c" />


`client`

<img width="789" height="180" alt="image" src="https://github.com/user-attachments/assets/adf79707-7e2a-4beb-bfa8-519fe882f88d" />


---

## RESULT
Thus the Python program for socket communication using HTTP protocol for webpage upload and download was executed successfully.
