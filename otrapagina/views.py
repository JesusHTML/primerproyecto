from django.shortcuts import render

# Create your views here.


def principal2(request):  # Siempre se pasa como parametro request
    return render(request, 'otrapagina/principal2.html')  # render renderiza 
                #peticion    #archivo

# En templates crearemos los html