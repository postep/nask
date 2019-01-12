from apscheduler.schedulers.background import BackgroundScheduler
from http.server import BaseHTTPRequestHandler, HTTPServer

import datetime
import time

import json



sched = BackgroundScheduler()

def my_interval_job():
	print (datetime.datetime.now())
sched.add_job(my_interval_job, 'interval', seconds=0.1)
sched.start()


class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		response = self.handle_http(self.path)
		self.wfile.write(response)

	def handle_http(self, path):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		r = {'is_claimed': 'True', 'rating': 3.5}
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