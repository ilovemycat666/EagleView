import schedule
import time
from daily_logs import pull_logs
from xL_maker import create

def job():
	print("It's 9:00am! Pulling logs...")
	variables = pull_logs()
	create(variables[0], variables[1], variables[2])
	print("All logs have been pulled.")
	return

# job()
schedule.every().day.at("09:00").do(job)

while True:
	schedule.run_pending()
	time.sleep(59) # wait one minute!