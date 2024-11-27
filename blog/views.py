from django.shortcuts import render
from .models import Post

# Create your views here.

def principal(request):  # Siempre se pasa como parametro request
    posts = Post.objects.all()
    autores = Post.objects.values_list('autor', flat=True).distinct() # Con esto vamos a cojer a todos los autores pero no repetiremos sus nombres
    return render(request, 'blog/principal.html' , {'posts':posts , 'autores':autores})       # render renderiza 
                #peticion         #archivo             #Creo un dicionario





# En templates crearemos los html