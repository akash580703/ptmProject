from django.db import models


class Whatsapp(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=100)
    doc = models.CharField(max_length=100)
    pages = models.IntegerField()
    printed = models.IntegerField()
    amount = models.IntegerField()
    paid = models.IntegerField()
    inDate = models.CharField(max_length=100, default='---------')


# Create your models here.
