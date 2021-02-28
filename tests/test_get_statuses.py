import unittest
import json
import os
import shutil
from maciej_device_monitor import get_statuses


class TestGettingStatuses(unittest.TestCase):
    def test_output(self):
        os.mkdir("test_devices")
        with open('test_devices/fridge.json', 'w') as device1:
            data = {'voltage': 230, 'current': 10}
            json.dump(data, device1)
        with open('test_devices/tv.json', 'w') as device2:
            data = {'isEnabled': True}
            json.dump(data, device2)
        expected_output = {'fridge': {'current': 10, 'voltage': 230}, 'tv': {'isEnabled': True}}
        self.assertEqual(expected_output, get_statuses("test_devices"))
        shutil.rmtree('test_devices')


if __name__ == '__main__':
    unittest.main()
