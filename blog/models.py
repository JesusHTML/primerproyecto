from django.db import models

# Create your models here.
class Autor (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dni = models.CharField(unique=True, max_length=9)
    bio = models.TextField(blank=0 , verbose_name="biografía") # Esto es para que no sea obligatorio , que se pueda quedar en blanco
    
    class Meta:
        verbose_name="Autor"
        verbose_name_plural = "Autores"
    

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE) # Importante la foreingkey
    cuerpo = models.TextField() # Si no se pone nada es un campo obligatorio
    fechasP = models.DateField()

    def __str__(self):
        return f"Nombre post: {self.titulo} , id {self.id}"