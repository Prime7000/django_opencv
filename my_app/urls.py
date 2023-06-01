from django.urls import path
from . import views
from .views import *

app_name = 'cv'

urlpatterns = [
    path('', views.grayscale_view, name='filter_image'),
    
]
