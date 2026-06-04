from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Etudiant, Classe, Module, Filiere, Avis, Note
from .forms import EtudiantForm, ModuleForm, FiliereForm, ClasseForm, AvisForm, NoteForm


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
    search = request.GET.get('q', '')
    etudiants = Etudiant.objects.all()
    if search:
        etudiants = etudiants.filter(
            nom__icontains=search
        ) | etudiants.filter(
            prenom__icontains=search
        ) | etudiants.filter(
            classe__icontains=search
        )
    return render(request, 'scolaire/etudiant_liste.html', {
        'etudiants': etudiants,
        'search': search
    })

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
    search = request.GET.get('q', '')
    modules = Module.objects.all()
    if search:
        modules = modules.filter(
            nom__icontains=search
        ) | modules.filter(
            enseignant__icontains=search
        ) | modules.filter(
            filiere__icontains=search
        )
    return render(request, 'scolaire/module_liste.html', {
        'modules': modules,
        'search': search
    })


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
    search = request.GET.get('q', '')
    filieres = Filiere.objects.all()
    if search:
        filieres = filieres.filter(
            nom__icontains=search
        ) | filieres.filter(
            description__icontains=search
        )
    return render(request, 'scolaire/filiere_liste.html', {
        'filieres': filieres,
        'search': search
    })


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
    search = request.GET.get('q', '')
    classes = Classe.objects.all()
    if search:
        classes = classes.filter(
            nom__icontains=search
        ) | classes.filter(
            filiere__icontains=search
        ) | classes.filter(
            niveau__icontains=search
        )
    return render(request, 'scolaire/classe_liste.html', {
        'classes': classes,
        'search': search
    })


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

@login_required(login_url='/accounts/login/')
def etudiant_detail(request, pk):
    etudiant = get_object_or_404(Etudiant, id=pk)
    avis = Avis.objects.filter(etudiant=etudiant)
    return render(request, 'scolaire/etudiant_detail.html', {
        'etudiant': etudiant,
        'avis': avis
    })


# ─── NOTES ───
@login_required(login_url='/accounts/login/')
def note_liste(request):
    # Etudiant voit seulement ses propres notes
    if request.user.groups.filter(name='Etudiant').exists():
        # On cherche l'étudiant lié à cet utilisateur par son nom
        notes = Note.objects.filter(
            etudiant__nom__icontains=request.user.username
        ) | Note.objects.filter(
            etudiant__prenom__icontains=request.user.username
        )
    else:
        notes = Note.objects.all().order_by('etudiant', 'semestre')

    # Calcul moyenne par étudiant
    from django.db.models import Avg
    moyenne = notes.aggregate(Avg('note'))['note__avg']

    return render(request, 'scolaire/note_liste.html', {
        'notes': notes,
        'moyenne': moyenne
    })


@login_required(login_url='/accounts/login/')
def note_ajouter(request):
    if not (request.user.is_superuser or request.user.groups.filter(name='Professeur').exists()):
        messages.error(request, 'Accès refusé.')
        return redirect('note_liste')
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note ajoutée avec succès !')
            return redirect('note_liste')
    return render(request, 'scolaire/note_form.html', {'form': form, 'titre': 'Ajouter une note'})


@login_required(login_url='/accounts/login/')
def note_modifier(request, pk):
    if not (request.user.is_superuser or request.user.groups.filter(name='Professeur').exists()):
        messages.error(request, 'Accès refusé.')
        return redirect('note_liste')
    note = get_object_or_404(Note, id=pk)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note modifiée avec succès !')
            return redirect('note_liste')
    return render(request, 'scolaire/note_form.html', {'form': form, 'titre': 'Modifier une note'})


@login_required(login_url='/accounts/login/')
def note_supprimer(request, pk):
    if not (request.user.is_superuser or request.user.groups.filter(name='Professeur').exists()):
        messages.error(request, 'Accès refusé.')
        return redirect('note_liste')
    note = get_object_or_404(Note, id=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note supprimée avec succès !')
        return redirect('note_liste')
    return render(request, 'scolaire/note_confirm_supprimer.html', {'note': note})