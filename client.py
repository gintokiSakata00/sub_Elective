import socket
import webbrowser
import os
from newscript import html_template
  
host = socket.gethostname()
port = 8000

my_pyscript = []
my_pyscript.append("<py-script>")
status=0
anime = ""
try:
    connection = socket.socket() 
    connection.connect((host, port))
    my_pyscript.append("pyscript.write('port', 'Port: {}')".format(port))
    count = 0
    status =1
    with open ('password_list.txt', 'r') as password:
        for key_pass in password:
            connection.sendall(key_pass.encode("utf-8"))
            reply = connection.recv(1024).strip().decode()
            if count ==0:
                print("Wrong Password Below")
            if reply == "Congratulations Dear Hacker!, don't forget to create a tutorial":
                print()
                hack = "HACKED COMPLETED!"
                print(hack)
                my_pyscript.append("pyscript.write('status','Status: {}')".format(hack))
                true_pass ="PASSWORD: "+key_pass.strip()
                print(true_pass)
                my_pyscript.append("pyscript.write('password', 'Password: {}')".format(key_pass.strip()))
               
            else:
                    count+=1  
                    print("Line: {} X: {}".format(count,key_pass.strip()))
except socket.error:
    if status == 0:
        print("Error in Connection")
        my_pyscript.append("pyscript.write('port', 'Port: {}')".format(port))
        my_pyscript.append("pyscript.write('status', 'Status: HACKED FAILED')")
        my_pyscript.append("pyscript.write('password', 'Password: Unknown')")
        anime = "sad"
    else:
        anime = "happy"
finally:
    connection.close()
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

    



