from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import api_views

router = DefaultRouter()
router.register(r'etudiants', api_views.EtudiantViewSet)
router.register(r'modules', api_views.ModuleViewSet)
router.register(r'classes', api_views.ClasseViewSet)
router.register(r'filieres', api_views.FiliereViewSet)
router.register(r'avis', api_views.AvisViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    # Étudiants
    path('etudiants/', views.etudiant_liste, name='etudiant_liste'),
    path('etudiants/ajouter/', views.etudiant_ajouter, name='etudiant_ajouter'),
    path('etudiants/<int:pk>/modifier/', views.etudiant_modifier, name='etudiant_modifier'),
    path('etudiants/<int:pk>/supprimer/', views.etudiant_supprimer, name='etudiant_supprimer'),
    # Modules
    path('modules/', views.module_liste, name='module_liste'),
    path('modules/ajouter/', views.module_ajouter, name='module_ajouter'),
    path('modules/<int:pk>/modifier/', views.module_modifier, name='module_modifier'),
    path('modules/<int:pk>/supprimer/', views.module_supprimer, name='module_supprimer'),
    # Filières
    path('filieres/', views.filiere_liste, name='filiere_liste'),
    path('filieres/ajouter/', views.filiere_ajouter, name='filiere_ajouter'),
    path('filieres/<int:pk>/modifier/', views.filiere_modifier, name='filiere_modifier'),
    path('filieres/<int:pk>/supprimer/', views.filiere_supprimer, name='filiere_supprimer'),
    # Classes
    path('classes/', views.classe_liste, name='classe_liste'),
    path('classes/ajouter/', views.classe_ajouter, name='classe_ajouter'),
    path('classes/<int:pk>/modifier/', views.classe_modifier, name='classe_modifier'),
    path('classes/<int:pk>/supprimer/', views.classe_supprimer, name='classe_supprimer'),
    # Avis
    path('avis/', views.avis_liste, name='avis_liste'),
    path('avis/ajouter/', views.avis_ajouter, name='avis_ajouter'),
    path('avis/<int:pk>/supprimer/', views.avis_supprimer, name='avis_supprimer'),
    # API
    path('api/', include(router.urls)),
    
    path('etudiants/<int:pk>/', views.etudiant_detail, name='etudiant_detail'),

    # Notes
    path('notes/', views.note_liste, name='note_liste'),
    path('notes/ajouter/', views.note_ajouter, name='note_ajouter'),
    path('notes/<int:pk>/modifier/', views.note_modifier, name='note_modifier'),
    path('notes/<int:pk>/supprimer/', views.note_supprimer, name='note_supprimer'),
]