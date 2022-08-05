from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import os
from Whatsapp.models import Whatsapp;
from Whatsapp.seriliazers import WhatsappSerializer;
from Whatsapp.razorpay import sendMsg

@csrf_exempt
def whatsAppApi(request,phone=0):

    if request.method == 'GET':

        WhatsappDoc = Whatsapp.objects.filter(phone=phone,printed=0).latest("phone")
        WhatsappDoc = WhatsappSerializer(WhatsappDoc)
        return JsonResponse(WhatsappDoc.data,safe=False)


    if request.method =='POST':
        WhatsappDocJson = JSONParser().parse(request)

        WhatsappDoc = WhatsappSerializer(data = WhatsappDocJson)

        if WhatsappDoc.is_valid():

            WhatsappDoc.save()
            return JsonResponse(True,safe=False)

        return JsonResponse(False,safe=False)


    if request.method == 'PUT':
        WhatsappDocJson = JSONParser().parse(request)
        WhatsappDoc = WhatsappSerializer(data = WhatsappDocJson)

        if WhatsappDoc.is_valid():
            WhatsappDoc.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

@csrf_exempt
def payment(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        print(data)
        return JsonResponse("Failed to Update.", safe=False)


@csrf_exempt
def testMe(request):
    if request.method == 'GET':
        return JsonResponse("Updated Successfully!!", safe=False)

