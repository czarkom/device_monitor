import unittest
import threading
import json
import os
import shutil
from maciej_device_monitor import start, stop


class TestStartingAndStoppingMonitor(unittest.TestCase):
    def test_start_and_stop(self):
        os.mkdir("test_devices")
        with open('test_devices/lamp.json', 'w') as device1:
            data = {'voltage': 230, 'current': 10}
            json.dump(data, device1)
        before = threading.active_count()
        start('test_devices', 1)
        after_start = threading.active_count()
        self.assertTrue(any(thread.name == 'Device_monitor_thread' for thread in threading.enumerate()))
        self.assertEqual(before, after_start - 1)
        stop()
        self.assertFalse(any(thread.name == 'Device_monitor_thread' for thread in threading.enumerate()))
        self.assertEqual(before, threading.active_count())
        shutil.rmtree('test_devices')


if __name__ == '__main__':
    unittest.main()
