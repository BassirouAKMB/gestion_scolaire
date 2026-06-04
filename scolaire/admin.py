from django.contrib import admin
from .models import Filiere, Niveau, Classe, Etudiant, Module, Avis
from .models import Filiere, Niveau, Classe, Etudiant, Module, Avis, Note

@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description']
    search_fields = ['nom']


@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description']
    search_fields = ['nom']


@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ['nom', 'filiere', 'niveau']
    list_filter = ['filiere', 'niveau']
    search_fields = ['nom']


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'email', 'classe', 'date_inscription']
    list_filter = ['classe']
    search_fields = ['nom', 'prenom', 'email']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['nom', 'enseignant', 'nbr_heures', 'filiere']
    list_filter = ['filiere']
    search_fields = ['nom', 'enseignant']


@admin.register(Avis)
class AvisAdmin(admin.ModelAdmin):
    list_display = ['etudiant', 'module', 'note', 'date_avis']
    list_filter = ['module', 'note']
    search_fields = ['etudiant__nom', 'module__nom']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['etudiant', 'module', 'note', 'semestre', 'date_ajout']
    list_filter = ['semestre', 'module']
    search_fields = ['etudiant__nom', 'module__nom']