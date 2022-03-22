from django.urls import path
from Web1MHApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('tratamientos', views.tratamientos, name="Tratamientos"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),
]