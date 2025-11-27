from django.contrib import admin
from django.urls import path
# from django.http import HttpResponse -> Pode ser removido, visto que quem o utiliza agora é o arquivo de views do app
from recipes.views import home, contato, sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]