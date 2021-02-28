"""
@Maciej Czarkowski
Test of device monitor. For the test issues I created "devices" directory with devices that should be observed.
If you'd like to edit some data, please ensure to pass correct directory name to functions and watch your syntax,
because if you don't, everything's gonna be logged and saved (parsing errors etc., just to let user know what's wrong)
I'm logging data to stderr and maciej_device_logs.log file to make it easier to notice every useful info.
"""

import time
import threading
import maciej_device_monitor as td

# At first, let's try to get all of the statuses using get_statuses method
td.get_statuses('devices')


print("Device monitor starting in a while...")
# Here I pass my directory with devices name and frequency of logging info about devices
td.start('devices', 1)

# We can have a look at our fresh thread and its name
for thread in threading.enumerate():
    print(thread.name)

# Here we are sleeping for a few seconds just to have a look how nicely our monitor is logging data about devices.
# It's possible to edit devices data on the fly, just save file and you can see fresh info logged.
time.sleep(10)

# We're done, so we can stop our device monitor
td.stop()

# Let's print out our thread and see that our device monitor is gone - just as it should
for thread in threading.enumerate():
    print(thread.name)

# Bye, bye:)
print("Exiting Main Thread")