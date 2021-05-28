"""PETShoping URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from PETApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('home/', views.homePage, name='home'),
    path('logout/', views.logoutUser, name='logout'),
    path('petReg/', views.petRegPage, name='petReg'),
    path('', views.nav, name='nav'),
    path('about/', views.about, name='about'),
    path('about1/', views.about1, name='about1'),
    path('display/', views.display_page, name='display'),
    path('home/buy/<int:pk>/', views.buy_pet, name='buy'),
    path('home/details/<int:pk>/', views.moreInfo, name='info'),
    path('success/', views.successPage, name='success'),
    path('payment/', views.payment, name='payment'),
    path('test/<type>/', views.getPet, name='test'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
