import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

auth_filename = 'auth.json'

class SpotifyControl():
    def __init__(self):
        scope = "user-library-read user-read-playback-state user-modify-playback-state"

        with open('auth.json', 'r') as auth_file:
            auth_dict = json.load(auth_file)

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                            client_id=auth_dict['client_id'],
                                                            client_secret=auth_dict['client_secret'],
                                                            redirect_uri=auth_dict['redirect_url']))

    def get_id(self, device_name):
        dev_list = self.sp.devices()['devices']

        for device in dev_list:
            name = device['name']
            id = device['id']
            if name == device_name:
                return id
        
        # Device not found
        return None
    
    def play(self, playlist_uri, device_id):
        self.sp.start_playback(device_id=device_id, uris=[playlist_uri])


if __name__ == '__main__':
    contr = SpotifyControl()
    denon = contr.get_id("Denon")
    contact_datf_punk = 'spotify:track:79koEJRtKOOGJ0VSAF3FMk'
    doiwannaknow = 'spotify:track:5FVd6KXrgO9B3JPmC8OPst'

    contr.play(playlist_uri=doiwannaknow,
               device_id=denon)