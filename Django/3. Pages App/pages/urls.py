from django.urls import path
from .views import HomePage , AboutPage , ContactPage , Base

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path('home/', HomePage.as_view(), name= 'home'),
    path('about/', AboutPage.as_view(), name= 'about'),
    path('contact/', ContactPage.as_view(), name= 'contact')
    
    
]
