# Generated by Django 3.2.2 on 2021-05-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210512_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebBusTimetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateField(auto_now_add=True)),
                ('region', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=20)),
                ('bus_num', models.CharField(max_length=10)),
                ('bus_start_point', models.CharField(max_length=100)),
                ('bus_end_point', models.CharField(max_length=100)),
                ('post_url', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=200)),
            ],
        ),
    ]
