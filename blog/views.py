from django.shortcuts import get_object_or_404, render , HttpResponsePermanentRedirect 
from .models import Autor, Post
from .forms import post_form , post_form_model , post_autores

# Create your views here.

def principal(request):  # Siempre se pasa como parametro request
    posts = Post.objects.all()
    autores = Post.objects.values_list('autor', flat=True).distinct() # Con esto vamos a cojer a todos los autores pero no repetiremos sus nombres
    return render(request, 'blog/principal.html' , {'posts':posts , 'autores':autores})       # render renderiza 
                #peticion         #archivo             #Creo un dicionario




def detalle_post(request, pk):
    post = Post.objects.get()   # ARREGLAR LO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #contex = get_object_or_404(Post , pk=pk)
    return render >(request, 'blog/detalle_post.html' , {'post': post})
# En templates crearemos los html

## CRUD autores
def autores(request):
    context = Autor.objects.all()
    return render(request, 'blog/autor.html', {'autores':context})

def detalle_autor(request , pk):
    autor = get_object_or_404(Autor , pk=pk)
    posts = Post.objects.filter(autor=autor) #Este 'autor' viene de la clase Post en el modelo
    return render(request , 'blog/autor_post.html' , {'autor':autor , 'posts': posts})

def autor_post(request , pk):
    autor = get_object_or_404(Autor , pk=pk)
    posts = Post.objects.filter(autor=autor) #Este 'autor' viene de la clase Post en el modelo
    return render(request , 'blog/autor_post.html' , {'autor':autor , 'posts': posts})

###

#--

def post_new(request):
    if request.method == "POST":
        form = post_form(request.POST)
        # ftitulo = request.POST['titulo']
        # fcuerpo = request.POST['cuerpo']
        # fpublicacion = request.POST['fpublicado']
        if form.is_valid():    # CUANDO LLEGA POR POST
            # FORM.SAVE()
            ftitulo = request.cleaned_data['titulo']
            fcuerpo = request.cleaned_data['cuerpo']
            fpublicacion = request.cleaned_data['fpublicado']

            autor = Autor.objects.get(id=1)
            #Post.objects.create(autor=1)
            Post.objects.create(titulo=ftitulo , autor=autor , cuerpo=fcuerpo , publicacion=fpublicacion)
            form = post_form()
    else:   # CUANDO LLEGA POR GET
        form = post_form()  # Dentro del parentesis instance=post

        return render(request , 'blog/new.html' , {'form': form})   # puede ser que este mal 
    

    def post_edit(request , pk):

        if request.method == "POST":
            form = post_form(request.POST)
            # ftitulo = request.POST['titulo']
            # fcuerpo = request.POST['cuerpo']
            # fpublicacion = request.POST['fpublicado']
            if form.is_valid():
                ftitulo = request.cleaned_data['titulo']
                fcuerpo = request.cleaned_data['cuerpo']
                fpublicacion = request.cleaned_data['fpublicado']

                autor = Autor.objects.get(id=1)
                #Post.objects.create(autor=1)
                Post.objects.create(titulo=ftitulo , autor=autor , cuerpo=fcuerpo , publicacion=fpublicacion)
                form = post_form()
        else:
            #form = post_form(initial=post.__dict__)                      #    MAPEO
            post = get_object_or_404(Post, pk=pk)
            form = post_form_model(instance=post)
            return render(request , 'blog/new.html' , {'form': form})
    


    








