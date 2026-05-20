from rest_framework import serializers
from .models import Etudiant, Module, Classe, Filiere, Avis


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = '__all__'


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'


class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class AvisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avis
        fields = '__all__'