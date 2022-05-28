from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

#Class del Tuitl
class Tuitl(models.Model):
    fecha = models.DateTimeField(default=datetime.now)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to = 'avatares', null=True, blank=True)
    #img = models.FileField(upload_to = 'media')
    
#Class del Avatar
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null=True, blank=True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"