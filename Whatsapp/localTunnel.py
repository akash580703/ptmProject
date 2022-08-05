import subprocess
import requests,threading,time
import sys
import os


variable = os.environ.get('myvar')


print("arugument " )
print(variable)


x= subprocess.Popen(
        "lt --port 8000 --subdomain " + variable, shell=True)
print(x)        

status=False


def server():
    global status
    n=0
    print("status")
    print(status)
    res=""
    print("res code")
    print(res)
    while status == False:
        time.sleep(4)

        #http: // akashptmproject.loca.lt/testMe/
        name = ["akashptmprojecthyderbad1",
                "akashptmprojecthyderbad2", "akashptmprojecthyderbad3"]
        try:
            print("23 localTunnel.py")
            res = requests.get("http://"+name[n]+".loca.lt/testMe/")


            print("res code2")
            print(res.status_code)

            if res.status_code == 200:
                status = True
        
            

                
            else:
                print(name[n])
                # subprocess.Popen(
                #     ["lt --port 8000 --subdomain ", name[n]], shell=True)

        except:
            pass               

        n+=1            


serverThread = threading.Thread(target=server)

# serverThread .setDaemon(True)
# serverThread.start()

