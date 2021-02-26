import time
import test_device as td
import threading

td.get_statuses('devices')
print("Zaraz startuje")
td.start('devices', 1)
time.sleep(5)
print("dupa")
time.sleep(4)
print("znow spalem")
td.stop()
#
# for thread in threading.enumerate():
#     print(thread.name)


print("dupa")
print("Exiting Main Thread")