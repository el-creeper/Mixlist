# Import des librairies
import sys
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
print(os.listdir())
import config


# Remplacez par vos identifiants d'application
SECRET_CLIENT_TOKEN = config.SPOTIFY_SECRET_CLIENT_TOKEN
CLIENT_ID = config.SPOTIFY_CLIENT_ID
REDIRECT_URI = config.REDIRECT_URI



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
