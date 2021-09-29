import json
import datetime
import random
# Load json file, make all the changes and save updated version
# If no file exist create a new one
# If file exist load it


class Alarm:
    def __init__(self, id=None, hour=0, minute=0, active=True, playlist_name=None, playlist_id=None):
        if id is None:
            self.id = random.randint(1,10**10)
        else:
            self.id = id
        self.hour = hour
        self.minute = minute
        self.active = True if active == 1 else False
        self.playlist_name = playlist_name
        self.playlist_id = playlist_id

    def check_time(self):
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
    
    def deactivate(self):
        self.active = False
    
    def activate(self):
        self.active = True

    def __str__(self) -> str:
        return f"Godz: {self.hour}:{self.minute}, Status: {self.active}, Playlist: {self.playlist_name} {self.playlist_id}"


class Alarms:
    def __init__(self, file_name=None):
        self.alarms = []
        self.file_name = file_name
        if file_name is not None:
            with open(self.file_name, 'r') as input:
                alarms_dict = json.load(input)
        if alarms_dict is not None:
            for alarm_dict in alarms_dict:
                self.alarms.append(Alarm(**alarm_dict))

    def __iter__(self):
        return iter(self.alarms)

    def print(self):
        for a in self.alarms:
            print(a)
    
    def save_to_json(self):
        with open(self.file_name, 'w') as output:
            new_list = self.to_dictionary()
            json.dump(new_list, output, indent=4)
    
    def to_dictionary(self):
        new_list = []
        for alarm in self.alarms:
            tmp_dict = {
                'id':alarm.id,
                'hour': alarm.hour,
                'minute': alarm.minute,
                'active': 1 if alarm.active else 0,
                'playlist_name': alarm.playlist_name,
                'playlist_id': alarm.playlist_id
            }
            new_list.append(tmp_dict)
        return new_list
    
    def add(self, time: datetime.time, playlist_id, playlist_name):
        new = Alarm(hour=int(time.strftime("%H")),
                    minute=int(time.strftime("%M")),
                    playlist_name=playlist_name,
                    playlist_id=playlist_id)
        print(new)
        self.alarms.insert(0, new)
    
    def remove(self, id=None):
        for i, al in enumerate(self.alarms):
            if al.id == id:
                self.alarms.pop(i)
                return




if __name__ == '__main__':
    a = Alarms("db.json")
    for k in a:
        print(k)
