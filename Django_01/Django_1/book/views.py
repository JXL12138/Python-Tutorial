from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.

def login(request):

    name = 'Jin'

    context = {'name': name}

    return render(request=request, context=context, template_name='login.html')
    # return HttpResponse('index')
