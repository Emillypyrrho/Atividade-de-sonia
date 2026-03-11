from django.urls import path
from . import views

urlpatterns = [
    path('pagina1/',views.pagina_inicial),
    path('pagina2/',views.pagina_sobre),
    path('pagina3/',views.pagina_projetos),
    path('pagina4/',views.pagina_contato),
]