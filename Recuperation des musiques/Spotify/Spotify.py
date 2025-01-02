# Import des librairies

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Remplacez par vos identifiants d'application
CLIENT_ID = "votre_client_id"
CLIENT_SECRET = "votre_client_secret"
REDIRECT_URI = "http://localhost:8080"

# Configuration OAuth
scope = "user-read-private"  # Permet de lire les informations utilisateur
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

# Récupérer les informations utilisateur
user_info = sp.current_user()
print("Nom d'utilisateur :", user_info['display_name'])
print("ID utilisateur :", user_info['id'])
