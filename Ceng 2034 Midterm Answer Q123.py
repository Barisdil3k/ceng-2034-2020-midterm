import os

import platform

platfrom_name = platform.platform()
cpu_cores = os.cpu_count()

print("PID is:", os.getpid())
print(f"The operating system is:", platfrom_name.title())
print("Numbers of CPU cores in the system is:", cpu_cores)

if "linux" in platfrom_name.lower():
    load_one_min, load_five_min, load_15_min = os.getloadavg()

    print("-------------load average-------------------------------")
    print("Load average over the last 1 minute:", load_one_min)
    print("Load average over the last 5 minutes:", load_five_min)
    print("Load average over the last 15 minutes:", load_15_min)
    print("---------------------------------------------------------")

    if cpu_cores - load_five_min < 0:
        print("Exiting the script...")
