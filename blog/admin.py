from django.contrib import admin

# Register your models here.


from .models import Post # Con esto importo la clase Post de models.py

admin.site.register(Post)
