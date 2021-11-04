import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

auth_filename = 'auth.json'

class SpotifyControl():
    def __init__(self):
        '''This class is for authenticating with spotify and controlling playback'''
        scope = "user-library-read user-read-playback-state user-modify-playback-state"

        with open('auth.json', 'r') as auth_file:
            auth_dict = json.load(auth_file)

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                            client_id=auth_dict['client_id'],
                                                            client_secret=auth_dict['client_secret'],
                                                            redirect_uri=auth_dict['redirect_url']))

    def get_id(self, device_name):
        '''Finds id of a device by its name'''
        dev_list = self.sp.devices()['devices']

        for device in dev_list:
            name = device['name']
            id = device['id']
            if name == device_name:
                return id
        
        # Device not found
        return None
    
    def play(self, playlist_uri, device_id):
        '''Start playback on a selected device'''
        self.sp.start_playback(device_id=device_id, context_uri=playlist_uri)


if __name__ == '__main__':
    contr = SpotifyControl()
    denon = contr.get_id("Galaxy S9")
    random_access_memories = "spotify:album:4m2880jivSbbyEGAKfITCa"

    contr.play(playlist_uri=random_access_memories,
               device_id=denon)