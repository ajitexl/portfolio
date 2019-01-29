from django.urls import path
from . import views #import views


# adding url
urlpatterns = [
    path('', views.index, name='home'), #home
    path('portfolio', views.portfolio, name='portfolio'), #portfolio
    path('contact', views.contact, name='contact'), #contact
    path('my_life', views.my_life, name='my_life')
]