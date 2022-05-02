from django.urls import path
from books.views import login

urlpatterns = [
    path('login/', login),

]
