import os
import json
from pathlib import Path


def get_statuses(devices_directory):
    data_dict = {}
    for filename in os.listdir(devices_directory):
        if filename.endswith(".json"):
            with open(devices_directory + '/' + filename) as json_file:
                data_dict[Path(filename).stem] = json.load(json_file)
    print(data_dict)
