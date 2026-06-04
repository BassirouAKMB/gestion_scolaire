from django import forms
from .models import Etudiant
from .models import Etudiant, Module, Filiere, Classe, Niveau, Avis, Note

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email', 'telephone', 'date_naissance', 'photo', 'classe']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'classe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: L1 Informatique'}),
        }

from .models import Etudiant, Module, Filiere


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['nom', 'enseignant', 'nbr_heures', 'filiere']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'enseignant': forms.TextInput(attrs={'class': 'form-control'}),
            'nbr_heures': forms.NumberInput(attrs={'class': 'form-control'}),
            'filiere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Informatique'}),
        }

from .models import Etudiant, Module, Filiere, Classe, Niveau


class FiliereForm(forms.ModelForm):
    class Meta:
        model = Filiere
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['nom', 'filiere', 'niveau']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'filiere': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau': forms.TextInput(attrs={'class': 'form-control'}),
        }


from .models import Etudiant, Module, Filiere, Classe, Niveau, Avis


class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['etudiant', 'module', 'message', 'note']
        widgets = {
            'etudiant': forms.Select(attrs={'class': 'form-select'}),
            'module': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'note': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 20}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['etudiant', 'module', 'note', 'semestre']
        widgets = {
            'etudiant': forms.Select(attrs={'class': 'form-select'}),
            'module': forms.Select(attrs={'class': 'form-select'}),
            'note': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 20, 'step': '0.25'}),
            'semestre': forms.Select(attrs={'class': 'form-select'}),
        }