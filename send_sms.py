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

numbers = ['+1' + line[8][1:4] + line[8][6:9] + line[8][10:] for line in pilots]

for line in pilots:
	if line[0] == 'JAV':
		print(f'''Hello, {line[7]} this is an automated request from EagleView. Our system shows you only have {line[9]} {line[5]} drives remaining. Please confirm your shipping address at the link below:''')

# group of phone numbers = ('#Phone numbers')

# # Your Account Sid and Auth Token from twilio.com/console
# # and set the environment variables. See http://twil.io/secure

# # account_sid = os.environ['#Some code']
# # auth_token = os.environ['#More code']
# account_sid = 'Your account sid'
# auth_token = 'your auth token'
# client = Client(account_sid, auth_token)

# for g in work_test:
# 	client.messages \
# 	    .create(
# 	         body=f"Hey this is eagle view, here's a drive request, please fill this out as soon as possible.\nhttps://eagleview.quickbase.com/db/bqt4z4hze?a=nwr",
# 	         from_='#A phone number',
# 	         to=g
# 	     )
