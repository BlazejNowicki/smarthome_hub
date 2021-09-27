from alarm_modules import Alarms, Alarm
from spotify_modules import SpotifyControl

def main():
    contr = SpotifyControl()
    denon = contr.get_id("Denon")
    contact_datf_punk = 'spotify:track:79koEJRtKOOGJ0VSAF3FMk'
    doiwannaknow = 'spotify:track:5FVd6KXrgO9B3JPmC8OPst'

    contr.play(playlist_uri=doiwannaknow,
               device_id=denon)


if __name__ == "__main__":
    main()