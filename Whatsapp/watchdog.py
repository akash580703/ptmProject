import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from Whatsapp.functions import main; 
x=True

class ExampleHandler(FileSystemEventHandler):
    def on_created(self, event): # when file is created
        # do something, eg. call your function to process the image
        print(122323)
        print(event.src_path, event.event_type)
        try:
   
          # sending message to receiver
          # using pywhatkit
            main()
            print("Successfully Sent!")

        except: 
            
            

          # handling exception
          # and printing error message
            print("An Unexpected Error!")

if x :
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