from network import LoRa
import socket
import time
import pycom

lora = LoRa(mode=LoRa.LORA, region=LoRa.AU915)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
pycom.heartbeat(False)

while True:
	s.send('Ping')
	print('Ping')
	pycom.rgbled(0xFF0000)
	time.sleep(1)

	pycom.rgbled(0x0000FF)
	print('Pause')
	time.sleep(4)
