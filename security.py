import sys
import time
from subprocess import call

import pymongo
from pymongo import MongoClient
import datetime

def write_alert(ip_str):
	client = MongoClient()
	client = MongoClient('localhost', 27017)

	db = client["alerts"]
	iptables_collection = db["iptables_block"]
	alert = {"ip": ip_str, "description": "try of nmap", "date": datetime.datetime.utcnow()}
	x = iptables_collection.insert_one(alert)
	print('noted in db', ip_str)

try:
	buff = ''
	while True:
		buff += sys.stdin.read(1)
		if buff.endswith('\n'):
			buff = buff[:-1]
			msg_list = buff.split('[**]')
			msg_id = msg_list[1].split(':')
			msg_nr = int(msg_id[1])
			if msg_nr == 1000001:
				msg_ip_list = buff.split('->')
				msg_ip_port = msg_ip_list[0].split(' ')
				msg_ip = msg_ip_port[-2].split(':')[0]
				print(msg_ip)
				print("wrong activity")
				call(['iptables', '-A', 'INPUT', '-s', msg_ip, '-j', 'DROP'])
				call(['iptables', '-I', 'FORWARD', '-d', msg_ip, '-j', 'DROP'])
				write_alert(msg_ip)
			buff = ''
except KeyboardInterrupt:
	sys.stdout.flush()
	pass
