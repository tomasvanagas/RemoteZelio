from pymodbus.client.sync import ModbusTcpClient
import time
import datetime

ipAddress = '<your ip address>'


client = ModbusTcpClient(ipAddress)
while True:
    print("Running")
    client.write_register(16, 1)
    time.sleep(15)
    client.write_register(16, 0)
    time.sleep(15)
