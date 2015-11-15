from django.db import models
from django.utils import timezone

class Banda(models.Model):
    banda = models.CharField(max_length=50)
    integrantes = models.CharField(max_length=50)
    foto = models.ImageField(upload_to = 'Fotos/')

    def __str__(self):
        return self.banda

class Cancione(models.Model):
    autor = models.ForeignKey('auth.User')
    banda = models.ForeignKey(Banda,null=True,blank=True)
    titulo = models.CharField(max_length=200)
    duracion = models.CharField(max_length=15,default='00:00')
    letra = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

