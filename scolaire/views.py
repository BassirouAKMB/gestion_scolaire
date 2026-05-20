from django.shortcuts import render
from .models import Etudiant, Classe, Module, Filiere

from django.contrib import messages
from django.shortcuts import redirect
from .forms import EtudiantForm

from django.contrib.auth.decorators import login_required

from .models import Etudiant, Classe, Module, Filiere, Niveau
from .forms import EtudiantForm, ModuleForm

from .models import Etudiant, Classe, Module, Filiere
from .forms import EtudiantForm, ModuleForm, FiliereForm, ClasseForm

from .models import Etudiant, Classe, Module, Filiere, Avis
from .forms import EtudiantForm, ModuleForm, FiliereForm, ClasseForm, AvisForm

@login_required(login_url='/accounts/login/') 
def etudiant_ajouter(request):
    form = EtudiantForm()
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Étudiant ajouté avec succès !')
            return redirect('etudiant_liste')
    return render(request, 'scolaire/etudiant_form.html', {'form': form, 'titre': 'Ajouter un étudiant'})


@login_required(login_url='/accounts/login/') 
def index(request):
    context = {
        'nb_etudiants': Etudiant.objects.count(),
        'nb_classes': Classe.objects.count(),
        'nb_modules': Module.objects.count(),
        'nb_filieres': Filiere.objects.count(),
        'derniers_etudiants': Etudiant.objects.order_by('-date_inscription')[:5],
    }
    return render(request, 'scolaire/index.html', context)

@login_required(login_url='/accounts/login/') 
def etudiant_liste(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'scolaire/etudiant_liste.html', {'etudiants': etudiants})

@login_required(login_url='/accounts/login/') 
def etudiant_modifier(request, pk):
    etudiant = Etudiant.objects.get(id=pk)
    form = EtudiantForm(instance=etudiant)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Étudiant modifié avec succès !')
            return redirect('etudiant_liste')
    return render(request, 'scolaire/etudiant_form.html', {'form': form, 'titre': 'Modifier un étudiant'})

@login_required(login_url='/accounts/login/') 
def etudiant_supprimer(request, pk):
    etudiant = Etudiant.objects.get(id=pk)
    if request.method == 'POST':
        etudiant.delete()
        messages.success(request, 'Étudiant supprimé avec succès !')
        return redirect('etudiant_liste')
    return render(request, 'scolaire/etudiant_confirm_supprimer.html', {'etudiant': etudiant})

@login_required(login_url='/accounts/login/')
def module_liste(request):
    modules = Module.objects.all()
    return render(request, 'scolaire/module_liste.html', {'modules': modules})


@login_required(login_url='/accounts/login/')
def module_ajouter(request):
    form = ModuleForm()
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Module ajouté avec succès !')
            return redirect('module_liste')
    return render(request, 'scolaire/module_form.html', {'form': form, 'titre': 'Ajouter un module'})


@login_required(login_url='/accounts/login/')
def module_modifier(request, pk):
    module = Module.objects.get(id=pk)
    form = ModuleForm(instance=module)
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            messages.success(request, 'Module modifié avec succès !')
            return redirect('module_liste')
    return render(request, 'scolaire/module_form.html', {'form': form, 'titre': 'Modifier un module'})


@login_required(login_url='/accounts/login/')
def module_supprimer(request, pk):
    module = Module.objects.get(id=pk)
    if request.method == 'POST':
        module.delete()
        messages.success(request, 'Module supprimé avec succès !')
        return redirect('module_liste')
    return render(request, 'scolaire/module_confirm_supprimer.html', {'module': module})


# ─── FILIÈRES ───
@login_required(login_url='/accounts/login/')
def filiere_liste(request):
    filieres = Filiere.objects.all()
    return render(request, 'scolaire/filiere_liste.html', {'filieres': filieres})


@login_required(login_url='/accounts/login/')
def filiere_ajouter(request):
    form = FiliereForm()
    if request.method == 'POST':
        form = FiliereForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filière ajoutée avec succès !')
            return redirect('filiere_liste')
    return render(request, 'scolaire/filiere_form.html', {'form': form, 'titre': 'Ajouter une filière'})


@login_required(login_url='/accounts/login/')
def filiere_modifier(request, pk):
    filiere = Filiere.objects.get(id=pk)
    form = FiliereForm(instance=filiere)
    if request.method == 'POST':
        form = FiliereForm(request.POST, instance=filiere)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filière modifiée avec succès !')
            return redirect('filiere_liste')
    return render(request, 'scolaire/filiere_form.html', {'form': form, 'titre': 'Modifier une filière'})


@login_required(login_url='/accounts/login/')
def filiere_supprimer(request, pk):
    filiere = Filiere.objects.get(id=pk)
    if request.method == 'POST':
        filiere.delete()
        messages.success(request, 'Filière supprimée avec succès !')
        return redirect('filiere_liste')
    return render(request, 'scolaire/filiere_confirm_supprimer.html', {'filiere': filiere})


# ─── CLASSES ───
@login_required(login_url='/accounts/login/')
def classe_liste(request):
    classes = Classe.objects.all()
    return render(request, 'scolaire/classe_liste.html', {'classes': classes})


@login_required(login_url='/accounts/login/')
def classe_ajouter(request):
    form = ClasseForm()
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classe ajoutée avec succès !')
            return redirect('classe_liste')
    return render(request, 'scolaire/classe_form.html', {'form': form, 'titre': 'Ajouter une classe'})


@login_required(login_url='/accounts/login/')
def classe_modifier(request, pk):
    classe = Classe.objects.get(id=pk)
    form = ClasseForm(instance=classe)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classe modifiée avec succès !')
            return redirect('classe_liste')
    return render(request, 'scolaire/classe_form.html', {'form': form, 'titre': 'Modifier une classe'})


@login_required(login_url='/accounts/login/')
def classe_supprimer(request, pk):
    classe = Classe.objects.get(id=pk)
    if request.method == 'POST':
        classe.delete()
        messages.success(request, 'Classe supprimée avec succès !')
        return redirect('classe_liste')
    return render(request, 'scolaire/classe_confirm_supprimer.html', {'classe': classe})


# ─── AVIS ───
@login_required(login_url='/accounts/login/')
def avis_liste(request):
    avis = Avis.objects.all().order_by('-date_avis')
    return render(request, 'scolaire/avis_liste.html', {'avis': avis})


@login_required(login_url='/accounts/login/')
def avis_ajouter(request):
    form = AvisForm()
    if request.method == 'POST':
        form = AvisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avis ajouté avec succès !')
            return redirect('avis_liste')
    return render(request, 'scolaire/avis_form.html', {'form': form, 'titre': 'Ajouter un avis'})


@login_required(login_url='/accounts/login/')
def avis_supprimer(request, pk):
    avis = Avis.objects.get(id=pk)
    if request.method == 'POST':
        avis.delete()
        messages.success(request, 'Avis supprimé avec succès !')
        return redirect('avis_liste')
    return render(request, 'scolaire/avis_confirm_supprimer.html', {'avis': avis})