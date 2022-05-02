from django.db.models import F
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from books.models import BookInfo


# Create your views here.

def login(request):
    book = BookInfo.objects.all()

    content = {
        'books': book
    }



    return render(request, 'index.html', content)

    # return HttpResponse
