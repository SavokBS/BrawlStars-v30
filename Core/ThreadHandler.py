import logging
import time
from threading import *

from Logic.Player import Player
from Logic.PacketsHelper import PacketsHelper
from Packets.Factory import messages

logging.basicConfig(filename="errors.log", level=logging.INFO, filemode="w")

def _(*args):
	print('[v30]', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()

class Thread(Thread):
	def __init__(self, client, address, clients):
		super().__init__()
		self.client = client
		self.address = address
		self.clients = clients
		self.player = Player()

	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				print("Receive Error!")
				break
			data += s
		return data

	def run(self):
		last_packet = time.time()
		try:
			while True:
				header = self.client.recv(7)
				if len(header) > 0:
					last_packet = time.time()
					packet_id = int.from_bytes(header[:2], 'big')
					packet_name = PacketsHelper.getMessageName(packet_id)
					length = int.from_bytes(header[2:5], 'big')
					data = self.recvall(length)
					print(f'[CLIENT] => ID: {packet_id}, Name: {packet_name}, Length: {length}')
					if packet_id in messages:
						message = messages[packet_id](self.client, self.player, data)
						message.decode()
						message.process()
				if time.time() - last_packet > 5:
					_(f"Client disconnected!")
					self.client.close()
					break
		except ConnectionAbortedError:
			_(f"Client disconnected! >>> conected clients: {self.clients}")
			self.client.close()
		except ConnectionResetError:
			_(f"Client disconnected! >>> conected clients: {self.clients}")
			self.client.close()
		except TimeoutError:
			_(f"Client disconnected! >>> conected clients: {self.clients}")
			self.client.close()