# Utiliser une image Python 3 officielle
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY app.py app.py

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut pour exécuter le script
CMD ["python", "app.py"]