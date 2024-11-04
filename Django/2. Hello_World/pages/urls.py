from django.urls import path
from .views import home_page_view ,about_view

urlpatterns = [
    
     path('',home_page_view ,name = 'home'),
     path('about/', about_view, name = 'about')
]