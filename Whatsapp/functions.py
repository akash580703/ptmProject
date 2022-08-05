import pyautogui
from threading import Timer
import cv2
import threading  
import easyocr  
import json
import requests
from Whatsapp.fileHandling import pdfPage,Price
from Whatsapp.razorpay import paymentLink,sendMsg
from datetime import datetime

# datetime object containing current date and time
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
print("localTunnel")
# reader = easyocr.Reader(['en'], model_storage_directory="/Users/akash/djangoApp/")
reader = "easyoc"
number=None

xy=paymentLink(1000, "+919937851826")



x=True

# link = paymentLink(int(100), '+918917205846')
# print(link)


# xy=sendMsg("link","+919937851826",0)
# print(xy)


class ExampleHandler(FileSystemEventHandler):
    def on_created(self, event): # when file is created
        # do something, eg. call your function to process the image
        print(122323)
        print(event.src_path, event.event_type)
        src = event.src_path
        srcAry = src.split("/")
        
        try:
            phone = "+91"+srcAry[-1][:10]
            doc = srcAry[-1]
            pages = pdfPage(src)
            printed=0
            amount = Price(20, pages)
            paid = 0
            inDate = srcAry[-1][10:-4]

            data={

                "phone": phone,
                "doc": doc,
                "pages":pages,
                "printed":0,
                "amount": amount,
                "paid": paid,
                "inDate": inDate,

            }



            print(data)

            # data=json.loads(data)

            response = requests.post(
                'http://127.0.0.1:8000/pdf/', data=json.dumps(data))
            print(response.status_code)
            if response.status_code == 200:
                print(f"response {response}")
                link = paymentLink(int(amount),phone)
                # print(link)
                if link != None:
                    print("send Msg")
                    
                    sendMsg(link["short_url"], phone, 0)
                




   
          # sending message to receiver
          # using pywhatkit
        

        except: 
            
            

          # handling exception
          # and printing error message
            print("An Unexpected Error!")

def watcgDog():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = ExampleHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/Users/akash/Downloads')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


t = threading.Thread(target=watcgDog)
t.setDaemon(True)
t.start()

#  python manage.py runserver
# dd/mm/YY H:M:S

def toggleMsg():
    pyautogui.hotkey('ctrl', 'shift','tab')
    
def toggleDock():
    pyautogui.hotkey('command', 'shift','d')
 
def toggleNotf():
    pyautogui.hotkey('command', 'i')
    
def locateWpIcon(x):
    return pyautogui.locateCenterOnScreen(x)



def wpOcr(img,cord):
    cropped = img[cord[0]:cord[1], cord[2]:cord[3]]
#     cropped = im2[y:y + h, x:x + w]
    cv2.imwrite("wpScreenCrop.jpg", cropped)
    result = reader.readtext(cropped,allowlist="0123456789",detail=0)
    return result

def phoneNum():
    print("Num thread started")
    global number
    now = datetime.now()
    dt_string = now.strftime("%d%m%H%M")	
    pyautogui.click(x=533, y=29,clicks=2, interval=1,button='left')
    pyautogui.leftClick(x=533, y=29)

    pyautogui.screenshot('wpScreen.jpg')

    img=cv2.imread("wpScreen.jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    num=wpOcr(gray,[342,365,1185,1288])
    number= num[0]+dt_string
    print(number)
    print("Num thread Completed")

def saveFile():
    print("save thread Started")
    global number
    
    downloadFound=locateWpIcon("/Users/akash/ANPRwithPython/download.jpg") 
    print(f"downloadFound :{downloadFound}")
    if downloadFound!=None:
        pyautogui.leftClick(x=779, y=691)
    
    

    
    
#     pyautogui.leftClick(x=downloadFound.x, y=downloadFound.y)
    
    saveIcon=locateWpIcon("/Users/akash/ANPRwithPython/save.jpg") 

    print(f"saveIcon :{saveIcon}")

    
    while saveIcon==None:
        saveIcon=locateWpIcon("/Users/akash/ANPRwithPython/save.jpg")  
        print(f"saveIcon :{saveIcon}")

    print(f"saveIcon number :{number}")   
    pyautogui.typewrite(number, interval=0)

    print(f"Typeed number ") 

    
    pyautogui.hotkey('enter')
    print("save thread Completed")


def main(request):

    pyautogui.hotkey('command', 'w')

    wpIcon=locateWpIcon("/Users/akash/ANPRwithPython/wpHome.jpg") 
    


    print(f"wpIcon :{wpIcon}")

    
    while wpIcon==None:
        wpIcon=locateWpIcon("/Users/akash/ANPRwithPython/wpHome.jpg")  
        print(f"wpIcon ::{wpIcon}") 
        
    pyautogui.leftClick(x=wpIcon.x, y=wpIcon.y) 
    
    iconFound=locateWpIcon("/Users/akash/ANPRwithPython/wpStart.jpg") 
    print(f"iconFound :{iconFound}")
    
    while iconFound==None:
        iconFound=locateWpIcon("/Users/akash/ANPRwithPython/wpStart.jpg")
        
    notfMsg= pyautogui.locateAllOnScreen("/Users/akash/ANPRwithPython/wpAppNf1.jpg") 
    notfMsg=list(notfMsg)
    
    print(f"notfMsg :{notfMsg}")
    while len(notfMsg)==0:
        notfMsg=pyautogui.locateAllOnScreen("/Users/akash/ANPRwithPython/wpAppNf1.jpg")
        notfMsg=list(notfMsg)

        if len(notfMsg)==0:
            notfMsg=pyautogui.locateAllOnScreen("/Users/akash/ANPRwithPython/download.jpg")
            notfMsg=list(notfMsg)

        
    notfMsg=list(notfMsg)
    print(f"notfMsg ::{notfMsg}")
    lasrCordX=notfMsg[-1][0]-40
    lasrCordY=notfMsg[-1][1]+10
    
    
    print(f"x {lasrCordX}")
    print(f"y {lasrCordY}")
    

    pyautogui.leftClick(x=lasrCordX, y=lasrCordY)
#     .click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
    
    numThread = threading.Thread(target=phoneNum)
    numThread.start()

    saveThread=threading.Thread(target=saveFile)
    

    numThread.join()

    saveThread.start()
    saveThread.join()

 




    
    
    
    
    
#     pyautogui.leftClick(x=saveIcon.x, y=saveIcon.y) 
    
    
    
    
    
#     pyautogui.moveTo(x=lasrCordX, y=lasrCordY)
    
    
   
    
