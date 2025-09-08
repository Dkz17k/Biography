from django.urls import path
from biography.views import index

urlpatterns = [
    path('', index)
]