from django import forms
from .models import Utilisateur, Projet, Tache

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ('nom', 'email')

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ('nom', 'utilisateur')

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ('nom', 'description', 'projet')
