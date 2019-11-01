from pymodbus.client.sync import ModbusTcpClient
import time
import datetime

ipAddress = '172.16.0.190'


client = ModbusTcpClient(ipAddress)
while True:
    print("Running")
    client.write_register(16, 1)
    time.sleep(15)
    client.write_register(16, 0)
    time.sleep(15)
