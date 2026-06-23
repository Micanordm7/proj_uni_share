from django.http import HttpResponse


def home(request):
    """Vue pour la page d'accueil de UniShare"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>UniShare</title>
        <meta charset="utf-8">
    </head>
    <body style="font-family: Arial, sans-serif; margin: 40px; text-align: center;">
        <h1 style="color: #2c3e50;">Bienvenue sur UniShare !</h1>
        <p style="font-size: 18px; color: #7f8c8d;">La bourse aux livres et matériels académiques de l'université.</p>
        <hr style="width: 50%; margin: 30px auto;">
        <p style="color: #e74c3c; font-weight: bold;">Statut du projet : Phase 1 - Fondations MVT opérationnelles.</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)
