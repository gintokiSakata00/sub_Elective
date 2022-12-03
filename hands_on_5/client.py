import socket
import webbrowser
import os
from newscript import html_template
  
host = socket.gethostname()
port = 8000

my_pyscript = []
anime = ""

hack = true_pass= user_input = key_pass= ""
global count, status
count = status= 0        
def printResults(reply,key_pass,count):
    if "Congratulations" in reply:
        hack = "HACKED COMPLETED!"
        true_pass ="PASSWORD: "+key_pass
        print()
        print(hack)
        print(true_pass)
        return 1
    else:
        if count ==0:
            print("Wrong Password Below")
        count+=1  
        print("Line: {} X: {}".format(count,key_pass.strip()))
        return 0
    
try:
    connection = socket.socket() 
    connection.connect((host, port))
    user_question = input(str("Guess Mode \t[1]\nHack Mode \t[2]\nGo: "))
    if user_question == "1":
        user_input=""
        while status==0 or "quit" not in user_input:
            user_input = input("Enter password (quit to exit):")
            connection.sendall(user_input.strip().encode("utf-8"))
            reply = connection.recv(1024).strip().decode()
            status = printResults(reply,key_pass,count)
    else:
        with open("password_list.txt",'r') as password:
            for key_pass in password:
                    connection.sendall(key_pass.strip().encode("utf-8"))
                    reply = connection.recv(1024).strip().decode()
                    status = printResults(reply,key_pass,count)
                    if status ==1 :
                        status+=1
                        break
                
except socket.error:
    print("Error in Connection")

finally:
    if status == 0:
      
        hack = "HACKED FAILED"
        count = "UNKNOWN"
        key_pass = "UNKNOWN"
        anime = "sad"
    else:
        
        anime = "happy"
    key_pass = user_input if user_input == "" else key_pass 
    my_pyscript.append("<py-script>")
    my_pyscript.append("pyscript.write('port', 'Port: {}')".format(port))
    my_pyscript.append("pyscript.write('status','Status: {}')".format(hack))
    my_pyscript.append("pyscript.write('guess','Guess: {}')".format(count))
    my_pyscript.append("pyscript.write('password', 'Password: {}')".format(key_pass))
    my_pyscript.append("</py-script>")
    my_pyscript.append('<div class="image">')
    if anime == "happy":
        my_pyscript.append('<img src="./images/happy.jpg" ></img>')
    else:
        my_pyscript.append('<img src="./images/sad.jpg" ></img>')
    my_pyscript.append("</div>")
    my_pyscript.append("</div>")
    my_pyscript.append("</body>")
    my_pyscript.append("</html>")
    
    html = open('index.html', 'w')
    for script in my_pyscript:
        html_template += script + "\n"
        
    # print(html_template)
    html.write(html_template)
    html.close()
    
    question = input(str('Open in browser? Y/N: '))
    if question.lower() == 'y':        
        filename = 'file:///'+os.getcwd()+'/' + 'index.html'
        webbrowser.open_new_tab(filename)
    else:
        print("exited")
        
        
def printResults(reply,key_pass,count):
    if count ==0:
        print("Wrong Password Below")
    if "Congratulations" in reply:
        hack = "HACKED COMPLETED!"
        true_pass ="PASSWORD: "+key_pass.strip()               
    else:
            count+=1  
    print("Line: {} X: {}".format(count,key_pass.strip()))
    



