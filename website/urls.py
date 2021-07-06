"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from recordmgmt import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_records', views.list_records, name='list_records'),
    path('add_items', views.add_items, name='add_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('admin/', admin.site.urls),
    path('goals', views.goals, name='goals'),
    path('home', views.home, name='home'),
    path('people', views.people, name='people'),
    path('projects', views.projects, name='projects'),
    path('institutions', views.institutions, name='institutions'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.pricing, name='pricing'),
    path('faq', views.faq, name='faq'),
    path('blog-home',views.bloghome, name='blog-home')
]
