from django.urls import path

from . import views
from marketing.views import index
urlpatterns = [
    path('home/index.html', index),
    
 
]