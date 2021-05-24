import os
from twilio.rest import Client
from daily_logs import pull_logs, suggested

pilots = []
logs = pull_logs()
vendors = logs[0]
drive_counts = logs[1]
for v in vendors:
	for vendor in drive_counts:
		if vendor[0][0][0] == v:
			for group in vendor:
				# if v == 'JAV':
				# 	print(group)
				# 	print('-------')
				for line in group:
					boxes = suggested(len(group), line)
					if boxes == 'X':
						continue
					line.append(boxes)
					pilots.append(line)

# Creats numbers from pilots and transforms numbers, '(585) 703-1895' to, '+15857031895' for twilio
numbers = ['+1' + line[8][1:4] + line[8][6:9] + line[8][10:] for line in pilots]

for line in pilots:
	if line[0] == 'JAV':
		print(f'''Hello, {line[7]} this is an automated request from EagleView. Our system shows you only have {line[9]} {line[5]} drives remaining. Please confirm your shipping address at the link below:\nhttps://eagleview.quickbase.com/db/bqt4z4hze?a=nwr''')

# work_test = ('+15857031895', '+15857979340', '+13157194255')

# # Your Account Sid and Auth Token from twilio.com/console
# # and set the environment variables. See http://twil.io/secure

# # account_sid = os.environ['AC28ce78f51dc88ba514b50112ac6b5f2d']
# # auth_token = os.environ['c5eec11af22e4e72ed1b6f79e7e6c226']
# account_sid = 'AC28ce78f51dc88ba514b50112ac6b5f2d'
# auth_token = 'c5eec11af22e4e72ed1b6f79e7e6c226'
# client = Client(account_sid, auth_token)

# for g in work_test:
# 	client.messages \
# 	    .create(
# 	         body=f"Hey this is eagle view, here's a drive request, please fill this out as soon as possible.\nhttps://eagleview.quickbase.com/db/bqt4z4hze?a=nwr",
# 	         from_='+14243484582',
# 	         to=g
# 	     )
