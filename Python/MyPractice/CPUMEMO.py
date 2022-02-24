import psutil



print(psutil.cpu_percent())
print(psutil.virtual_memory().percent)

print(psutil.sensors_temperatures())