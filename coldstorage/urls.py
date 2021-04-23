from django.urls import path 
from .views import *

urlpatterns = [
    path('', index_view, name='home')
    # path('show/<str:name>', show_view, name='show')
]
