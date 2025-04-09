import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from spotipy.oauth2 import SpotifyOAuth
# load the .env file variables
load_dotenv()

# Spotify API credentials

# Crear instancia de Spotipy con autenticación
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

#Nombres de todos los albunes

eminem='spotify:artist:7dGJo4pcD2V6oG8kP0tJRR'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

#print(dir(spotipy.Spotify)) atributos y metodos de la libreria

results = spotify.artist_top_tracks(eminem)
#print(help(spotify.artist_top_tracks))

songs = []
for track in results['tracks']:
    songs.append({
        'name': track['name'],
        'popularity': track['popularity'],
        'duration_min': track['duration_ms'] / 60000
        
    })
track_ids = [track["id"] for track in results["tracks"]]
#features = sp.audio_features('7lQ8MOhq6IN2w8EYcFNSUk')
#print((track_ids))

df = pd.DataFrame(songs)
df_sorted = df.sort_values(by="popularity", ascending=False)
print(df_sorted[['name', 'popularity']].head(3))

plt.scatter(df["popularity"], df["duration_min"], color ="red")
plt.xlabel("Popularidad")
plt.ylabel("Duración (min)")
plt.title("Duración vs Popularidad de Canciones")
plt.savefig("Duración vs Popularidad de Canciones.png")
plt.show()


