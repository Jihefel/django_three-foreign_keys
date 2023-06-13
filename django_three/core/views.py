from django.shortcuts import render, redirect
from .forms import UtilisateurForm, ProjetForm, TacheForm
from .models import Utilisateur, Projet, Tache

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def creer_utilisateur(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_utilisateurs')
    else:
        form = UtilisateurForm()
    return render(request, 'core/creer_utilisateur.html', {'form': form})

def creer_projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_projets')
    else:
        form = ProjetForm()
    return render(request, 'core/creer_projet.html', {'form': form})

def creer_tache(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_taches')
    else:
        form = TacheForm()
    return render(request, 'core/creer_tache.html', {'form': form})

def liste_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'core/liste_utilisateurs.html', {'utilisateurs': utilisateurs})

def utilisateur_details(request, id):
    utilisateurs = Utilisateur.objects.all()
    utilisateur = utilisateurs.get(id=id)
    projets = Projet.objects.all().filter(utilisateur=id)
    taches = Tache.objects.all().filter(projet__utilisateur_id=id)
    # taches = Tache.objects.filter(projet__utilisateur_id=id) : 
    # Filtre les tâches en utilisant le double soulignement __ pour accéder aux attributs de la clé étrangère. 
    # Ici, nous filtrons les tâches en fonction de l'ID de l'utilisateur associé via le projet.
    return render(request, 'core/utilisateur_details.html', {'utilisateur': utilisateur, 'taches': taches, 'projets': projets})

def liste_projets(request):
    projets = Projet.objects.all()
    return render(request, 'core/liste_projets.html', {'projets': projets})

def liste_taches(request):
    taches = Tache.objects.all()
    return render(request, 'core/liste_taches.html', {'taches': taches})

def tache_details(request, id):
    taches = Tache.objects.all()
    tache = taches.get(id=id)
    return render(request, 'core/tache_details.html', {'tache': tache})
