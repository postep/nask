from apscheduler.schedulers.background import BackgroundScheduler
from http.server import BaseHTTPRequestHandler, HTTPServer

import datetime
import time

import json

import queue

import simulation

HOST_NAME = '20.0.0.1'
PORT_NUMBER = 9000

global u_queue
u_queue = queue.Queue()
u = 0

p = simulation.Process()
sched = BackgroundScheduler()
class SimProcess():
	def __init__(self):
		self.u = 0

	def job(self, u_queue):
		while not u_queue.empty():
			self.u = u_queue.get()
			print('get', self.u)
		s = p.next_step(self.u)


sim = SimProcess()
sched.add_job(sim.job, 'interval', [u_queue], seconds=simulation.DT)
sched.start()



class MyHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		try:
			u = float(self.path[1:])
			u_queue.put(u)
		except:
			pass
		response = self.handle_http(self.path)
		self.wfile.write(response)

	def handle_http(self, path):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		[state, y] = p.get_safe_state()
		r = {'status': 'OK', 'state': state, 'y': y}
		content = json.dumps(r)
		return bytes(content, 'UTF-8')

if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))