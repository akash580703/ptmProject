from rest_framework import serializers
from Whatsapp.models import  Whatsapp


class WhatsappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whatsapp
        fields = ("id",
                  "phone",
                  "doc",
                  "pages",
                  "printed",
                  "amount",
                  "paid",
                  "inDate",
       )
