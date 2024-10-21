from django.db import models
from django.contrib.auth.models import User



class User_id(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="no avatar")



class Messenger(models.Model):
    author = models.ForeignKey(User_id, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    message = models.TextField()



class Chat(models.Model):
    author = models.ForeignKey(User_id, on_delete=models.CASCADE)
    message = models.TextField()




