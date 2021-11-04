from alarm_modules import Alarms
from spotify_modules import SpotifyControl
from datetime import datetime


def main():
    contr = SpotifyControl()
    denon = contr.get_id('Galaxy S9')
    all = Alarms('db.json')
    now = datetime.now()

    print(f'Checking for active alarms...  ({now.strftime("%H:%M:%S")})')
    any_alarm_triggered = False
    for alarm in all:
        if alarm.check_time():
            print('Alarm triggered:', alarm)
            contr.play(playlist_uri=alarm.playlist_id,
                       device_id=denon)
            alarm.deactivate()
            any_alarm_triggered = True

    if any_alarm_triggered:
        print('Updating json file')
        all.save_to_json()


if __name__ == "__main__":
    main()
