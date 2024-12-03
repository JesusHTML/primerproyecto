from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    cuerpo = models.TextField()
    fecha = models.DateField() # NUEVO CAMPO INTRODUCIDO  

    def __str__(self):
        return f"El autor {self.autor} escribio el post {self.titulo} el dia {self.fecha}"
