import time
import maciej_device_manager as td
import threading

td.get_statuses('devices')
print("Zaraz startuje")
td.start('devices', 1)
# for thread in threading.enumerate():
#     print(thread.name)
time.sleep(5.2)
print("dupa")
time.sleep(4)
print("znow spalem")
td.stop()
time.sleep(5)
# for thread in threading.enumerate():
#     print(thread.name)

print("Exiting Main Thread")