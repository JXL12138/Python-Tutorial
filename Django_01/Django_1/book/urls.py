from django.urls import path
from book.views import login

urlpatterns = [

        path("login/", login),

]