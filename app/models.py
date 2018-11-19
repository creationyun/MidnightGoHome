from django.db import models

# Create your models here.
class KakaoService(models.Model):
    user = models.CharField(max_length=100, primary_key=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    # dhcp_status = models.BooleanField(default=False)
    nightbus_status = models.BooleanField(default=False)
    paidtoilet_status = models.BooleanField(default=False)

class WebGuideRequests(models.Model):
    user = models.CharField(max_length=100)
    request_time = models.DateTimeField(auto_now_add=True)
    startpoint = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)

class WebGuideReplies(models.Model):
    reply_time = models.DateTimeField(auto_now_add=True)
    request_id = models.IntegerField()
    reply_content = models.TextField(blank=True)
