import time
import test_device as td
import threading

td.start('devices', 1)
time.sleep(5)
td.stop()
#
# for thread in threading.enumerate():
#     print(thread.name)


print("dupa")
print("Exiting Main Thread")