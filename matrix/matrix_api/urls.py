from django.urls import path
from .views import *


urlpatterns = [
    path('userCheck/', user_handler.as_view(), name='user'),
]
