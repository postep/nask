#!/usr/bin/python3

import threading, time
import urllib.request, urllib.error

HOST_NAME = '20.0.0.1'


class attack_thread(threading.Thread):
	def run(self):
		port = 54
		while True:
			url_str = 'http://'+HOST_NAME+':'+str(port)
			print('connection:', url_str)
			try:
				connection = urllib.request.urlopen(url_str, timeout=1)
				connection.getcode()
			except:
				pass
			if port > 1000:
				port = 54
			else:
				port += 1


try:
	for _ in range(3):
		thread=attack_thread()
		thread.daemon=True
		thread.start()
	while True:
		time.sleep(100)
except (KeyboardInterrupt, SystemExit):
	print('\nReceived keyboard interrupt, quitting attack.\n')
