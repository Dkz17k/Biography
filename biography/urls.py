from django.urls import path
from biography.views import index
from biography.views import contato

urlpatterns = [
    path('', index),
    path('contato/', contato, name='contato')
]