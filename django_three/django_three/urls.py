"""
URL configuration for azz project.

The  list routes URLs to views. For more information please see:
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('utilisateur/creer/', views.creer_utilisateur, name='creer_utilisateur'),
    path('projet/creer/', views.creer_projet, name='creer_projet'),
    path('tache/creer/', views.creer_tache, name='creer_tache'),
    path('utilisateur/liste/', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('projet/liste/', views.liste_projets, name='liste_projets'),
    path('tache/liste/', views.liste_taches, name='liste_taches'),
    path('tache/<int:id>/', views.tache_details, name='tache_details'),
    path('utilisateur/<int:id>/', views.utilisateur_details, name='utilisateur_details'),
]
