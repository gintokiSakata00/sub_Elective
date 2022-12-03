import socket

host = socket.gethostname()
port = 8000


s = socket.socket() 
s.connect((host, port))

count=0
with open("password_list.txt",'r') as password:
        for key_pass in password:   
            count+=1 
            s.sendall(key_pass.encode("utf-8"))
            reply = s.recv(1024).strip().decode()
            if "hacker" in reply:
                print(str(count)+"  "+reply)


s.close()