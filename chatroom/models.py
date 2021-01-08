from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class massage(models.Model):
    athor = models.ForeignKey(User, verbose_name=("نویسنده"), on_delete=models.CASCADE)
    matnpayam = models.TextField(max_length=50000)
    date = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse("chatroom:rootchat")