# Import des librairies
import sys
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
import config


# Remplacez par vos identifiants d'application
CLIENT_SECRET = config.SPOTIFY_SECRET_CLIENT_TOKEN
CLIENT_ID = config.SPOTIFY_CLIENT_ID
REDIRECT_URI = config.REDIRECT_URI



# Configuration OAuth
scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

# Récupérer les informations utilisateur
user_info = sp.current_user()
playlists = sp.current_user_playlists()
liste_nom_playlists = [l["name"] for l in playlists["items"]]
lien = sp.current_user_saved_tracks()["items"]
print([e["track"]["name"] for e in lien])

def get_music_from_playlists(playlists):
     return [playlists["items"][i]["track"] for i in playlists["items"] if playlists["items"][i]["track"]["type"] == "track"]