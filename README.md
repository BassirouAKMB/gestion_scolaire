# 🎓 Gestion Scolaire — Application Django

Une application web complète de gestion scolaire développée avec Django 6 et Python 3.14.

---

## 🚀 Fonctionnalités

- ✅ Gestion des Étudiants (CRUD complet)
- ✅ Gestion des Modules
- ✅ Gestion des Classes
- ✅ Gestion des Filières
- ✅ Gestion des Avis
- ✅ Authentification (Login / Logout)
- ✅ Upload de photos
- ✅ API REST avec Django REST Framework
- ✅ Interface Admin Django personnalisée
- ✅ Design Bootstrap 5

---

## 🛠️ Technologies utilisées

| Technologie | Version |
|---|---|
| Python | 3.14 |
| Django | 6.0.5 |
| Django REST Framework | 3.x |
| Bootstrap | 5.3 |
| SQLite | (développement) |
| Pillow | 12.x |
| Gunicorn | (production) |
| Whitenoise | (production) |

---

## ⚙️ Installation locale

### 1. Cloner le projet
```bash
git clone https://github.com/BassirouAKMB/gestion_scolaire.git
cd gestion_scolaire
```

### 2. Créer l'environnement virtuel
```bash
python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # Mac/Linux
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations
```bash
python manage.py migrate
```

### 5. Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```

Accède à l'application sur **http://127.0.0.1:8000**

---

## 📁 Structure du projet

```
gestion_scolaire/
├── accounts/           # Authentification (login/logout)
│   ├── views.py
│   └── urls.py
├── config/             # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── scolaire/           # Application principale
│   ├── models.py       # Modèles de données
│   ├── views.py        # Vues
│   ├── forms.py        # Formulaires
│   ├── urls.py         # URLs
│   ├── admin.py        # Interface admin
│   ├── serializers.py  # Serializers API REST
│   └── api_views.py    # Vues API REST
├── templates/          # Templates HTML
│   ├── base/
│   │   └── base.html
│   ├── accounts/
│   │   └── login.html
│   └── scolaire/
│       ├── index.html
│       ├── etudiant_liste.html
│       ├── module_liste.html
│       ├── classe_liste.html
│       ├── filiere_liste.html
│       └── avis_liste.html
├── static/             # Fichiers CSS/JS
│   └── css/
│       └── style.css
├── media/              # Photos uploadées
├── requirements.txt    # Dépendances Python
├── Procfile            # Configuration Railway
└── README.md
```

---

## 🔗 API REST

Base URL : `/api/`

| Endpoint | Méthode | Description |
|---|---|---|
| `/api/etudiants/` | GET, POST | Liste et création d'étudiants |
| `/api/etudiants/{id}/` | GET, PUT, DELETE | Détail, modification, suppression |
| `/api/modules/` | GET, POST | Liste et création de modules |
| `/api/modules/{id}/` | GET, PUT, DELETE | Détail, modification, suppression |
| `/api/classes/` | GET, POST | Liste et création de classes |
| `/api/filieres/` | GET, POST | Liste et création de filières |
| `/api/avis/` | GET, POST | Liste et création d'avis |

> ⚠️ Toutes les routes API nécessitent une authentification.

---

## 🌐 URLs principales

| URL | Description |
|---|---|
| `/` | Tableau de bord |
| `/etudiants/` | Liste des étudiants |
| `/modules/` | Liste des modules |
| `/classes/` | Liste des classes |
| `/filieres/` | Liste des filières |
| `/avis/` | Liste des avis |
| `/accounts/login/` | Connexion |
| `/accounts/logout/` | Déconnexion |
| `/admin/` | Interface admin Django |
| `/api/` | API REST |

---

## 🔒 Sécurité

- Protection CSRF activée
- Cookies HTTP only
- Protection contre le clickjacking (X-Frame-Options)
- Variables sensibles via variables d'environnement
- Authentification requise sur toutes les pages

---

## 🚀 Déploiement sur Railway

1. Connecte-toi sur [railway.app](https://railway.app)
2. Clique **New Project** → **Deploy from GitHub**
3. Sélectionne le repo `gestion_scolaire`
4. Ajoute les variables d'environnement :
   - `SECRET_KEY` → ta clé secrète
   - `DEBUG` → `False`
5. Railway déploie automatiquement ✅

---

## 👤 Auteur

**Bassirou AKMB**
- GitHub : [@BassirouAKMB](https://github.com/BassirouAKMB)

---

## 📝 Licence

Ce projet est open source et disponible sous licence MIT.
