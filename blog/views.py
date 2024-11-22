from django.shortcuts import render

# Create your views here.

def principal(request):  # Siempre se pasa como parametro request
    return render(request, 'blog/principal.html')  # render renderiza 
                #peticion    #archivo

# En templates crearemos los html