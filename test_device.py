import os
import json
from pathlib import Path
import threading
import time

exitFlag = False


class DeviceManagerThread (threading.Thread):
    def __init__(self, devices_directory, frequency):
        threading.Thread.__init__(self)
        self.devices_directory = devices_directory
        self.frequency = frequency

    def run(self):
        while not exitFlag:
            get_statuses(self.devices_directory)
            time.sleep(self.frequency)


def start(devices_directory, frequency):
    thread = DeviceManagerThread(devices_directory, frequency)
    thread.start()


def stop():
    global exitFlag
    exitFlag = True


def get_statuses(devices_directory):
    data_dict = {}
    for filename in os.listdir(devices_directory):
        if filename.endswith(".json"):
            with open(devices_directory + '/' + filename) as json_file:
                data_dict[Path(filename).stem] = json.load(json_file)
    print(data_dict)
