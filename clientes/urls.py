from django.urls import path
from .views import *

urlpatterns = [
    path('list/', person_list, name='person_list'),
    path('new/', person_new, name='person_new'),
    path('update/<int:id_person>', person_update, name='person_update'),
    path('delete/<int:id_person>', person_delete, name='person_delete'),
]
