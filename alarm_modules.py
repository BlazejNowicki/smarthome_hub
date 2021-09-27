import json
import datetime
# Load json file, make all the changes and save updated version
# If no file exist create a new one
# If file exist load it


class Alarm:
    def __init__(self, hour=0, minute=0, active=0, playlist_id=None):
        self.hour = hour
        self.minute = minute
        self.active = True if active == 1 else False
        self.playlist_id = playlist_id

    def check(self):
        '''Check if alarm should be executed'''
        now = datetime.datetime.now().replace(microsecond=0)
        two_min_ago = now - datetime.timedelta(minutes=2)
        alarm_time = now.replace(hour=self.hour,
                                 minute=self.minute, 
                                 second=0,
                                 microsecond=0)
        # print(now)
        # print(two_min_ago)
        # print(alarm_time)
        return self.active and two_min_ago <= alarm_time <= now

    def __str__(self) -> str:
        return f"Godz: {self.hour}:{self.minute}, Status: {self.active}, Playlist's id: {self.playlist_id}"


class Alarms:
    def __init__(self, file_name=None):
        self.alarms = []
        if file_name is not None:
            with open(file_name, 'r') as input:
                alarms_dict = json.load(input)
        if alarms_dict is not None:
            for alarm_dict in alarms_dict:
                self.alarms.append(Alarm(**alarm_dict))

    def __iter__(self):
        return iter(self.alarms)

    def print(self):
        for a in self.alarms:
            print(a)


if __name__ == '__main__':
    a = Alarms("db.json")
    # a.print()
    for k in a:
        print(k)
        k.check()