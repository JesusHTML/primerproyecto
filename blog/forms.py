from django import forms
from .models import Post , Autor


class post_form (forms.form):
    titulo = forms.CharField(label="Titulo" , max_length=200)
    cuerpo = forms.CharField(label='cuerpo', widget= forms.Textarea)
    fpublicado = forms.DateField(label='Fecha de publicacion')
    

# class post_form_model (forms.ModelForm):
#     fpublicado = forms.DateField(label='Fecha de la publicación',
#                                  input_formats=['%d/%m/%Y','%Y/%m/%d'],
#                                  "name": Textarea(attrs={"cols": 80, "rows": 20}))

class autores_form (forms.form):
    nombre = forms.CharField(label="nombre", max_length=100)
    apellido = forms.CharField(label="apellido" , max_length=100)
    email= forms.EmailField(label="email")
    dni= forms.


class Meta:
    model = Post
    fields = '__all__' #Con esto tomo todos los campos de post , tambien se puede hacer de otra forma
    