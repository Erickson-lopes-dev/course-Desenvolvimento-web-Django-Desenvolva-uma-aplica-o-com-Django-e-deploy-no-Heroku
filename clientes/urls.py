from django.urls import path
from .views import *

urlpatterns = [
    path('list/', person_list),
]
