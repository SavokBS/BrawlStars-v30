import socket
from Core.ThreadHandler import Thread

class Server:
	def __init__(self, ip: str, port: int):
		self.server = socket.socket()
		self.port = port
		self.ip = ip
		self.clients = 0

	def start(self):
		self.server.bind((self.ip, self.port))
		print(f'TCP server listening on {self.ip}:{self.port}')
		while True:
			self.server.listen()
			client, address = self.server.accept()
			self.clients += 1
			print(f'New connection! >>> connected clients: {self.clients}')
			Thread(client, address, self.clients).start()