import socket
port = int(input("Enter port"))
host = input("enter host")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(3)
    try:
        print("========================")
        print("     WEB SCANNER")
        print("========================")
        print("Host:", host)
        print("Port:", port)
        print() 
        s.connect((host,port))
        print("Port Status: OPEN")
        request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
        s.send(request.encode())
        response = s.recv(4096)
        text=response.decode()
        parts = text.split("\r\n\r\n")
        headers = parts[0].split("\r\n")
        frame_found = False
        csp_found = False
        hsts_found = False
        for line in headers:
           if line.startswith("X-Frame-Options:"):
              frame_found = True
              frame_value = line.split(":",1)[1].strip()
           if line.startswith("Content-Security-Policy:"):
              csp_found = True
              csp_value = line.split(":",1)[1].strip()
           if line.startswith("Strict-Transport-Security: "):
              hsts_found = True
              hsts_value = line.split(":",1)[1].strip()
           if line.startswith("HTTP/"):
              http = line.split(" ",2)[1].strip()
           if line.startswith("Server:"):
             server = line.split(":", 1)[1].strip()
           if line.startswith("Content-type:") :
             content = line.split(":",1)[1].strip()
           if line.startswith("Content-Length: "):
             length = line.split(":",1)[1].strip()
        if frame_found == False :
           print("X-Frame-Options: Missing")
        else:
           print(f"X-Frame-Options: {frame_value}")
        if csp_found == False:
           print("Content-Security-Policy : Missing ")
        else:
           print(f"Content-Security-Policy :{csp_value}")
        if hsts_found == False:
           print("Strict-Transport-Security: Missing ")
        else:
           print(f"Strict-Transport-Security: {hsts_value} ")
        print(f"Http Status: {http}")  
        print(f"Server: {server}")
        print(f"Content-type : {content}")
        print(f"Length: {length}")          
    except Exception as error:
     print("Error:", error)
     