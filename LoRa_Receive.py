from network import LoRa
import socket
import time
import pycom
from machine import UART

lora = LoRa(mode=LoRa.LORA, region=LoRa.AU915)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
pycom.heartbeat(False)

uart = UART(1, 9600)

count=0

while True:
	pycom.rgbled(0X000000)
	time.sleep(1)
	data = s.recv(64)
	print(data)
	data_conv = str(data)
	print(data_conv)
	print(str(count))
	count = count + 1

	for i in range(data_conv)
		print(i)
		uart.write(i)
	uart.write('\r')
	if data==b'Ping':
		s.send('Pong')
		pycom.rgbled(0xFF0000)
		time.sleep(1)
	pycom.rgbled(0x0000FF)
	time.sleep(4)