from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('<int:pk>', views.detalle_post , name='detalle_post') ,  #Para pasar otro parametro en la url  <int:pk>/...
    path('new' , views.post_new, name='post_new'),
    path('blog/new' , views.post_new , name='post_new' ),
    path('blog/edit/<int:pk>' , views.post_edit , name='post_edit' ),

    
    path('autores/', views.autores , name='autores'),
    path('autor/<int:pk>/' , views.detalle_post , name='detalle_autor'),
    
]