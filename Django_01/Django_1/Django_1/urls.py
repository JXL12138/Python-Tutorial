"""Django_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""
1. urlsoatterns 是固定写法
2. 值是列表类型
3. 在浏览器中输入的路径会在 urlspatterns 中顺序匹配，匹配成功直接进入相应的模块，如果匹配不成功直接返回404
 

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('book.urls')),
]
