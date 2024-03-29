"""musicex URL Configuration

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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),  # ajouter ce motif sous notre autre motif de groupes
    path('bands/<int:id>/change', views.band_update, name='band-update'),
    path('bands/add/', views.band_create, name='band-create'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('listings/', views.listings, name='list-ads'),
    path('listings/<int:id>/', views.listing_detail, name='ad-detail'),
    path('listings/<int:id>/change', views.listing_update, name='ad-update'),
    path('listings/add/', views.listing_create, name='listing-create'),
    path('confirmation/', views.redirectPage, name='email-sent'),
]
