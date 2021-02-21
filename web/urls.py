from django.urls import path
from .views import (
    index,
    home,
    about,
    news,
    contact,
    destinations,
    elements
)
urlpatterns = [
    path('',index, name="home" ),
    path('home/',home, name="home" ),
    path('about/',about, name="about" ),
    path('news/',news, name="news" ),
    path('destinations/',destinations, name="destinations" ),
    path('elements/',elements, name="elements" ),
    path('contact/',contact, name="contact" ),
]
