# %%

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read user-read-playback-state user-modify-playback-state"
client_id = "a4b661f55c6a499399de495677750087"
client_secret = "6f99d7271ab14a49a247be8c66dad03c"
redirect_url = "http://127.0.0.1:9090"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, 
                     client_secret=client_secret, redirect_uri=redirect_url))

results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
# %%
target_id_phone = None
dev_list = sp.devices()['devices']
for device in dev_list:
    name = device['name']
    id = device['id']
    print(name, id)
    if name == 'Galaxy S9':
        target_id_phone = id
    if name == 'Denon':
        target_id_denon = id

song_uri = 'spotify:track:79koEJRtKOOGJ0VSAF3FMk'
print(target_id_phone, song_uri)



# %%
# print(sp.next_track())

# %%
# Play Motherboard by Daft Punk on Galaxy S9
if sp and target_id_phone and song_uri:
    sp.start_playback(device_id=target_id_phone, uris=[song_uri])

# %%
# Tranfer playback to Denon
# if target_id_phone:
#     sp.transfer_playback(device_id=target_id_denon)

# %%
