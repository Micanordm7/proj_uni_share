from django.contrib import admin
from .models import Departement, Categorie, Annonce

# Enregistrement de la catégorie
admin.site.register(Categorie)


# --- CONFIGURATION DE L'AFFICHAGE DES DEPARTEMENTS ---
@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    # Liste des colonnes visibles dans le tableau de bord
    list_display = ('code', 'nom')
    # Permet de rendre le champ de recherche opérationnel sur le nom et le code
    search_fields = ('nom', 'code')


# --- CONFIGURATION DE L'AFFICHAGE DES ANNONCES ---
@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
    # 1. Optimisation de la vue en liste (Affichage en colonnes claires)
    list_display = ('titre', 'departement', 'nature', 'prix', 'date_publication', 'est_disponible')
    
    # 2. Ajout de filtres latéraux dynamiques (Très utile pour naviguer dans les annonces)
    list_filter = ('nature', 'est_disponible', 'departement', 'date_publication')
    
    # 3. Barre de recherche textuelle globale
    search_fields = ('titre', 'description')
    
    # 4. Organisation de la fiche d'édition en sections thématiques (Fieldsets)
    fieldsets =(('Informations Générales', {'fields': ('titre', 'description', 'departement')}),('Détails de l\'Échange', {'fields': ('nature', 'prix', 'categories')}),('Statut de Publication', {'fields': ('est_disponible',)}),)
    
