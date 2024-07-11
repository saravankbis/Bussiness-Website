"""
URL configuration for Parvathi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from press import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from press.views import check_email_existence


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('About/', views.About, name="About"),
    path('Contact/', views.Contact, name="Contact"),
    path('addData/', views.addData, name="addData"),
    path('Portfolio/', views.Portfolio, name="Portfolio"),
    path('Sign/', views.Sign, name="Sign"),
    path('Helpcenter/', views.Helpcenter, name="Helpcenter"),
    path('Prodcts/', views.Products, name="Products"),
]
urlpatterns += staticfiles_urlpatterns()

