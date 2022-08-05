import razorpay
import csv
import pywhatkit
from uritemplate import variables
from Whatsapp import localTunnel


linkCallback = "http://"+localTunnel.variable+".loca.lt/payment/"

def paymentLink(price,phone):
    global linkCallback
    print("linkCallback ")
    print(linkCallback)

    key = ""
    secret = ""

    global client
    data = {
            "amount": price,
            "currency": "INR",
            "description": "Printing",
            "customer": {
                "name": "phone",
                "email": "580akash@gmail.com",
                "contact": phone
            },
            "notify": {
                "sms": False,
                "email": False,
            },
            "reminder_enable": True,
            "callback_url": linkCallback,
        
            "callback_method": "get"

            }
    print(data)

    with open('/Users/akash/Downloads/rzp.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        key = (rows[1][0])
        secret=(rows[1][1])
        print(key + " "+secret)
        client = razorpay.Client(
            auth=(key, secret))

        print(client)

        
    # try:
    link = client.payment_link.create(data)

    print("payment link ")
    print(link)

    

    # except:

    #     link= None



    return link

    
   

def sendMsg(link,phone,img):
    if img == 0:

        pywhatkit.sendwhatmsg_instantly(
            phone, link,)
    if img != 0:

        pywhatkit.sendwhats_image(phone,img)


