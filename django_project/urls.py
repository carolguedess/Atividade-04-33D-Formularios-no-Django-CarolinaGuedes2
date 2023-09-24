"""django_project URL Configuration

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
from django.urls import path
from carolsapp import views

urlpatterns = [
  path('', views.home,name="home"),
  path('sucessos',views.create_sucesso),
  path('sucessos/update/<id>',views.update_sucesso),
  path('sucessos/delete/<id>',views.delete_sucesso),
  path('transformacao',views.create_transformacao),
  path('transformacao/update/<id>',views.update_transformacao),
  path('transformacao/delete/<id>',views.delete_transformacao),
  path('admin/', admin.site.urls),
]