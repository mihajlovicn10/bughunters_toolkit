"""
URL configuration for bughunters project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from toolkit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('scan/', views.scan_ports, name='scan_ports'),
    path('headers/', views.analyze_headers, name='analyze_headers'),
    path('bruteforce/', views.bruteforce_simulation, name='bruteforce_simulation'),
    path('download/', views.download_report, name='download_report'),
    path('security-practices/', views.security_practices, name='security_practices'),
    path('download/<str:report_type>/', views.download_report, name = "download_report"),
]


