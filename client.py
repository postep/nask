from apscheduler.schedulers.background import BackgroundScheduler

import urllib.request
import json
import time

import simulation

HOST_NAME = '20.0.0.1'
PORT_NUMBER = 9000
UC = 25

sched = BackgroundScheduler()
class SimProcess():
	def __init__(self):
		self.c = simulation.Controller(0.7, 0.5, 0.2)
		self.first_run = True
		self.u = None
		self.y = None

	def job(self):
		url_str = 'http://'+HOST_NAME+':'+str(PORT_NUMBER)
		if self.first_run:
			self.first_run = False
		else:
			if self.u:
				url_str += '/'+str(self.u)
		print(url_str)
		try:
			contents = urllib.request.urlopen(url_str).read()
			json_contents = json.loads(contents.decode('utf-8'))
			self.y = json_contents['y']
			print(self.y)
			self.u = self.c.next_step(UC-self.y)
			print(self.u)
		except:
			self.first_run = True

sim = SimProcess()
sched.add_job(sim.job, 'interval', seconds=simulation.DT)
sched.start()


while True:
	time.sleep(1)

