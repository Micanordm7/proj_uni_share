from django.db import models
from django.urls import reverse  # Utilisé pour formater et inverser les URLs dynamiques

class Departement(models.Model):
    """Représente un département académique ou une faculté de l'université."""
    nom = models.CharField(
        max_length=100, 
        verbose_name="Nom du département",
        help_text="Exemple : Informatique, Sciences Comptables, Génie Civil"
    )
    code = models.CharField(
        max_length=10, 
        unique=True, 
        verbose_name="Code court"
    )

    class Meta:
        ordering = ['nom']
        verbose_name = "Département"

    def __sub__(self):
        # Méthode obligatoire pour afficher proprement l'objet dans l'administration
        return f"{self.code} - {self.nom}"


class Categorie(models.Model):
    """Étiquettes ou tags applicables aux annonces (ex: Livre, Outil, Gratuit)."""
    libelle = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.libelle


class Annonce(models.Model):
    """Représente une petite annonce de matériel publiée par un étudiant."""
    
    # Types de transactions possibles (LOAN_STATUS / Choix fixes)
    TYPE_OFFRE = [
        ('DON', 'Don (Gratuit)'),
        ('PRET', 'Prêt temporaire'),
        ('VENTE', 'Vente à prix réduit'),
    ]

    titre = models.CharField(max_length=200, help_text="Quel objet proposez-vous ?")
    description = models.TextField(max_length=1000, help_text="Décrivez l'état du matériel, l'édition (si livre), etc.")
    prix = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, help_text="Laissez à 0.00 si c'est un don ou un prêt")
    nature = models.CharField(max_length=5, choices=TYPE_OFFRE, default='DON', help_text="Nature de l'échange")
    date_publication = models.DateTimeField(auto_now_add=True)  # Enregistre la date automatiquement à la création
    est_disponible = models.BooleanField(default=True, verbose_name="Disponible")

    # Clé Étrangère : Une annonce est liée à un département académique ciblé
    departement = models.ForeignKey(
        'Departement', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        help_text="Filière particulièrement concernée par ce matériel (optionnel)"
    )

    # Relation Many-to-Many : Une annonce peut avoir plusieurs tags/catégories
    categories = models.ManyToManyField(Categorie, help_text="Sélectionnez une ou plusieurs catégories")

    class Meta:
        # Les annonces les plus récentes s'affichent en premier (signe moins)
        ordering = ['-date_publication']
        verbose_name = "Annonce"

    def __str__(self):
        return f"{self.titre} ({self.get_nature_display()})"

    def get_absolute_url(self):
        """Retourne l'URL permettant d'accéder à la fiche détaillée d'une annonce."""
        return reverse('annonce-detail', args=[str(self.id)])
