'''This module loads json file, makes changes to alarms and saves updated version.'''

import json
import datetime
import random


class Alarm:
    def __init__(self, id=None, hour=0, minute=0, active=True, playlist_name=None, playlist_id=None):
        '''Object of this class stores information about one alarm.
        Args:
            id - alarm's id, if not specified will be assgined at random
            hour, minute - time for the alarm
            active - default state of the alarm
            playlist_name - under this name alarm will be visible on the configuration page
            playlist_id - URI number of a playlist - can be copied from Spotify
        '''
        if id is None:
            self.id = random.randint(10**9, 10**10-1)
        else:
            self.id = id
        self.hour = hour
        self.minute = minute
        self.active = True if active == 1 else False
        self.playlist_name = playlist_name
        self.playlist_id = playlist_id

    def check_time(self):
        '''Checks whether alarm should be executed'''
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
        '''Deactivate alarm'''
        self.active = False

    def activate(self):
        '''Activate alarm'''
        self.active = True

    def __str__(self) -> str:
        return f"Godz: {self.hour}:{self.minute}, Status: {self.active}, Playlist: {self.playlist_name} {self.playlist_id}"


class Alarms:
    def __init__(self, file_name=None):
        '''This class is a container for Alarm objects
        Args:
            file_name - file that contains alarms in json format
        '''
        self.alarms = []
        self.file_name = file_name
        if file_name is not None:
            with open(self.file_name, 'r') as input:
                alarms_dict = json.load(input)
        if alarms_dict is not None:
            for alarm_dict in alarms_dict:
                self.alarms.append(Alarm(**alarm_dict))

    def __iter__(self):
        # to make range-based for loop work
        return iter(self.alarms)

    def print(self):
        # for debugging
        for a in self.alarms:
            print(a)

    def save_to_json(self):

        with open(self.file_name, 'w') as output:
            new_list = self.to_dictionary()
            json.dump(new_list, output, indent=4)

    def to_dictionary(self):
        '''Returns dictionary representation'''
        new_list = []
        for alarm in self.alarms:
            tmp_dict = {
                'id': alarm.id,
                'hour': alarm.hour,
                'minute': alarm.minute,
                'active': 1 if alarm.active else 0,
                'playlist_name': alarm.playlist_name,
                'playlist_id': alarm.playlist_id
            }
            new_list.append(tmp_dict)
        return new_list

    def add(self, time: datetime.time, playlist_id, playlist_name):
        '''Add new alarm'''
        new = Alarm(hour=int(time.strftime("%H")),
                    minute=int(time.strftime("%M")),
                    playlist_name=playlist_name,
                    playlist_id=playlist_id)
        # print(new)
        self.alarms.insert(0, new)

    def remove(self, id=None):
        '''Remove alarm by id'''
        for i, al in enumerate(self.alarms):
            if al.id == id:
                self.alarms.pop(i)
                return


if __name__ == '__main__':
    # Print list of all alarms declared in db.json file
    a = Alarms("db.json")
    for k in a:
        print(k)
