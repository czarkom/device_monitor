import time
# we can use local version of script
import maciej_device_monitor as td

# but also we can use installed pip package:)
# import maciejdevicemonitor as td

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

print("Exiting Main Thread")