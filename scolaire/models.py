from django.db import models


class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Filière"
        verbose_name_plural = "Filières"


class Niveau(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Niveau"
        verbose_name_plural = "Niveaux"


class Classe(models.Model):
    nom = models.CharField(max_length=100)
    filiere = models.CharField(max_length=100, blank=True)
    niveau = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nom} - {self.filiere} - {self.niveau}"

    class Meta:
        verbose_name = "Classe"
        verbose_name_plural = "Classes"


class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='etudiants/', blank=True, null=True)
    classe = models.CharField(max_length=100, blank=True)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"


class Module(models.Model):
    nom = models.CharField(max_length=150)
    enseignant = models.CharField(max_length=150)
    nbr_heures = models.PositiveIntegerField(default=0)
    filiere = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"


class Avis(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='avis')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='avis')
    message = models.TextField()
    note = models.PositiveIntegerField(default=0)  # note sur 20
    date_avis = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avis de {self.etudiant} sur {self.module}"

    class Meta:
        verbose_name = "Avis"
        verbose_name_plural = "Avis"