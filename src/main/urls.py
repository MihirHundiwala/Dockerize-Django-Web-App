from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('game/<str:game>', views.gamepage, name='gamepage'),
    path('thanks', views.thanks, name='thanks'),
]
