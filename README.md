# 5a Create Socket for HTTP for Webpage Upload and Download

## AIM
To write a Python program for socket communication using HTTP protocol for webpage upload and download.

## ALGORITHM
1. Start server.
2. Create socket using Python socket module.
3. Bind server to localhost and port 5050.
4. Accept client requests.
5. Client sends GET request to download webpage.
6. Client sends POST request to upload data.
7. Server processes request and returns response.
8. Display output.
9. Stop program.

---

## FILES
- server.py
- client.py
- index.html
- upload.txt (generated)

---

## EXECUTION

```bash
python server.py
python client.py
```

## DOWNLOAD OPERATION
- Client sends HTTP GET request.
- Server returns webpage content.

## UPLOAD OPERATION
- Client sends HTTP POST request.
- Server stores uploaded data in upload.txt.

## RESULT
Thus the Python program for socket communication using HTTP protocol for webpage upload and download was executed successfully.
