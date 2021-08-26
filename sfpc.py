import requests
import csv
from bs4 import BeautifulSoup

def find():
# Pulls from QB, makes two lists for CIDs of Flying and Relfies tails
	url = 'https://eagleview.quickbase.com/db/[hidden url]'
	r = requests.get(url)
	with open('hidden path', 'wb') as f:
		f.write(r.content)
	reflies, flying = [], []
	with open('hidden path') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[2] == "Reflies Planned":
				reflies.append(row[1])
			elif row[2] == "Flying":
				flying.append(row[1])

# If a CID has a flight status of 'relfies in house' it is removed from its list (flying or reflies)
	r = requests.get('hidden URL')
	sauce = BeautifulSoup(r.text, "html.parser")
	tbody = sauce.find('tbody')
	trs = tbody.find_all('tr')
	for tr in trs:
		td = tr.find_all('td')
		if td[0].get_text().strip() in flying:
			if 'RefliesInHouse' in td[2].get_text().strip():
				# print(f'Flying:{td[0]}{td[2].get_text()}')
				cid = td[0].get_text().strip()
				flying.remove(cid)
		elif td[0].get_text().strip() in reflies:
			if 'RefliesInHouse' in td[2].get_text().strip():
				# print(f'Reflies:{td[0]}{td[2].get_text()}')
				cid = td[0].get_text().strip()
				reflies.remove(cid)


# Identifies plans with less than 5 missing lines
# + if reflies, skip CPIDs with 'refly' in name and 100% planned not received
	both = [reflies, flying]
	printer = []
	for j in both:
		print("---------------")
		for i in j:
			r = requests.get('hidden url')
			sauce = BeautifulSoup(r.text, "html.parser")
			count = 0
			for tr in sauce.find_all('tr')[4:]:
				tds = tr.find_all('td')
				name = tds[0].get_text().lower()
				planned = tds[4].get_text().split('(')
				planned = planned[1][:-2]
				if 'refly' in name and planned == '100':
					count += 6
					break
				if float(planned) > 20:
					count += 1
			if count < 5:
				print('hidden url')
				print(count)
				printer.append(i)

	for i in printer:
		print(i)

# errors happening due to fucking dolphin being slow as fugg
# need to find a implicit wait for bs4
