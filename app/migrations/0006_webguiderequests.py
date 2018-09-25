# Generated by Django 2.1.1 on 2018-09-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_kakaoservice_dhcp_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebGuideRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('request_time', models.DateTimeField(auto_now=True)),
                ('startpoint', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
    ]
