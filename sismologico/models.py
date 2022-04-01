from django.db import models
from django.contrib.auth.models import AbstractUser
import os
# Create your models here.
class User(AbstractUser):
    pass

class Sismo(models.Model):
    analista = models.CharField(max_length=8)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sismos_for_user')
    custom_id  = models.CharField(max_length=12)
    fecha = models.DateField()
    hora = models.TimeField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    profundidad = models.FloatField()
    magnitud = models.FloatField()
    comentario = models.CharField(max_length=150)
    magC= models.FloatField()
    magL = models.FloatField()
    magW = models.FloatField()
    rms = models.FloatField()
    sentido = models.BooleanField()
    data_estaciones = models.TextField(max_length=1024*6)
    date =  models.DateTimeField(auto_now_add=True)
    gapInfo = models.CharField(max_length=200,blank=True,default='')
    focalInfo = models.CharField(max_length=200,blank=True,default='')
    def serialize(self):
        return{
            'analista':self.analista,
            'id':self.id,
            'user':self.user.username,
            'custom_id':self.custom_id,
            'fecha':self.fecha,
            'hora':self.hora,
            'latitud':self.latitud,
            'longitud':self.longitud,
            'profundidad':self.profundidad,
            'magnitud':self.magnitud,
            'comentario':self.comentario,
            # 'analista':self.analista,
            'magC':self.magC,
            'magL':self.magL,
            'magW':self.magW,
            'rms':self.rms,
            'sentido':self.sentido,
            'data_estaciones':self.data_estaciones,
            'date':self.date.strftime("%b %d %Y, %H:%I %p"),
            'gapInfo':self.gapInfo,
            'focalInfo':self.focalInfo,
        }
    def __str__(self):
        return f'{self.fecha}  {self.hora}  {self.latitud}  {self.longitud}  {self.profundidad:>5}  {self.magnitud}  {self.comentario}'
    
class Article(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='articles_for_user')
    content =  models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    img_url = models.CharField(max_length=200)
    alt = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    article_url = models.CharField(max_length=200)
    # url = models.CharField(max_length=200)
    def serialize(self):
        return {
            'id':self.id,
            'user':self.user.username,
            'content':self.content,
            'preview_content':self.content[:300],
            'date':self.date.strftime("%b %d %Y, %H:%I %p"),
            'img_url':self.img_url.replace('\\','/'),
            'alt':self.alt,
            'title':self.title,
            'image_path': self.image_path.replace('\\','/'),
            'article_url': self.article_url,
            # 'url':self.url,
        }

    def __str__(self):
        return f'{self.title} |{self.user}'
