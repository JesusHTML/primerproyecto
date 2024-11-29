from django.contrib import admin

# Register your models here.


from .models import Post , Autor # Con esto importo la clase Post de models.py

admin.site.register(Post)
admin.site.register(Autor)
