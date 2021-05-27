import requests
import csv
from bs4 import BeautifulSoup

url = 'https://eagleview.quickbase.com/db/bpw3pr8ns?a=api_genresultstable&qid=34&options=csv&usertoken=b526ve_m8jc_0_c4paz38br5amh6bwm2cewciv5n6w'
r = requests.get(url)
with open(r'C:\Users\edwin.reik\Documents\programming\flight_tracker\flightsupport.csv', 'wb') as f:
	f.write(r.content)	
reflies, flying = [], []
with open(r'C:\Users\edwin.reik\Documents\programming\flight_tracker\flightsupport.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		if row[2] == "Reflies Planned":
			reflies.append(f'http://alpha.hq.eagleview.com/isdinfo/missing_imagery-output.php?strInputQuery={row[1]}&lines=aye')
		elif row[2] == "Flying":
			flying.append(f'http://alpha.hq.eagleview.com/isdinfo/missing_imagery-output.php?strInputQuery={row[1]}&lines=aye')

# print('---- Reflies Planned ----')
# for row in reflies:
# 	print(row)
# print('-------- Flying --------')
# for row in flying:
# 	print(row)

both = [reflies, flying]
for j in both:
	print("---------------")
	for i in j:
		r = requests.get(i)
		sauce = BeautifulSoup(r.text, "html.parser")
		count = 0
		for tr in sauce.find_all('tr')[4:]:
			tds = tr.find_all('td')
			planned = tds[4].get_text().split('(')
			planned = planned[1][:-2]
			if float(planned) > 20:
				count += 1
		if count < 5:
			print(f'{i}\n{count}')

# errors happening due to fucking dolphin being slow as fugg
# need to find a implicit wait for bs4

