# Generated by Django 3.2.4 on 2022-07-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Whatsapp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sn', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('doc', models.CharField(max_length=100)),
                ('pages', models.IntegerField()),
                ('printed', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('paid', models.IntegerField()),
                ('inDate', models.CharField(default='---------', max_length=100)),
            ],
        ),
    ]