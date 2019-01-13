import sys
import time
try:
	buff = ''
	while True:
		buff += sys.stdin.read(1)
		if buff.endswith('\n'):
			buff = buff[:-1]
			msg_list = buff.split('[**]')
			msg_id = msg_list[1].split(':')
			msg_nr = int(msg_id[1])
			
			if msg_nr == 10000001:
				print("normal activity")
			else:
				print("wrong activity")
				# TODO: send ssh iptables command
			buff = ''
except KeyboardInterrupt:
	sys.stdout.flush()
	pass