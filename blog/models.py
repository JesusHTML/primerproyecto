from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    cuerpo = models.TextField()

    def __str__(self):
        return f"Nombre post: {self.titulo} , id {self.id}"