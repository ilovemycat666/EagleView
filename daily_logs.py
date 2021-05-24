import requests 
import csv 
import time
import operator
from datetime import datetime


def pull_logs():
	url = 'https://eagleview.quickbase.com/db/bpw3pr8m9?a=api_genresultstable&qid=66&options=csv&usertoken=b526ve_m8jc_0_c4paz38br5amh6bwm2cewciv5n6w'
	r = requests.get(url)
	with open(r'C:\Users\edwin.reik\Documents\programming\dailypilotlogs\Daily_Pilot_Logs.csv', 'wb') as f:
		f.write(r.content)	

	with open(r'C:\Users\edwin.reik\Documents\programming\dailypilotlogs\Daily_Pilot_Logs.csv') as csvfile:
	    reader = csv.reader(csvfile)
	    logs = [row for row in reader]
	    logs.pop(0)

	vendors = set()
	hangars = set()
	rigs = set()
	logs_ = []

	# make sets and crops log list
	for log in logs:
		log = log[1:-2]
		vendors.add(log[0])
		hangars.add(log[1])
		rigs.add(log[6])
		log[-1] = int(log[-1])
		logs_.append(log)

	penta = []
	pacific = []
	canadian = []
	for hang in hangars:
		for vend in vendors:
			pen_group = []
			pac_group = []
			pen_can = []
			pac_can = []
			some = [log for log in logs_ if log[0] == vend and log[1] == hang]
			if some:
				for one in some:
					if one[5] == 'Penta':
						pen_group.append(one)
						if one[1].startswith('C'):
							pen_can.append(one)
					elif one[5] == 'Pacific':
						pac_group.append(one)
						if one[1].startswith('C'):
							pac_can.append(one)
					else:
						print('Camera System not Recognized')
						continue
			if pen_group:
				penta.append(pen_group)
			if pac_group:
				pacific.append(pac_group)
			if pen_can:
				canadian.append(pen_can)
			if pac_can:
				canadian.append(pac_can)

	canadian.sort()
	canadian.sort(key=(len), reverse=True)
	for c in canadian:
		c.sort(key=operator.itemgetter(-1))

	penta.extend(pacific)
	simple = [i for i in penta]

	add_average = []
	for group in simple:
		total = 0
		for line in group:
			total += int(line[-1])
		average = total / len(group)
		average = round(average, 2)
		total = 0
		for line in group:
			line.append(average)
		add_average.append(group)

	# groups the groups by vendor [vend[hang[line]]]
	by_vendor = []
	for v in vendors:
		vendor = [l for l in add_average if l[0][0] == v]
		by_vendor.append(vendor)

	by_vendor.sort()
	for vend_list in by_vendor:
		vend_list.sort(key=len, reverse=True)
		for group in vend_list:
			group.sort(key=operator.itemgetter(9))

	drive_count = [i for i in by_vendor]
	hangars = list(hangars)
	return vendors, drive_count, suggested, canadian, hangars

def suggested(group_len, line):
	length = int(group_len)
	average = line[-1]
	if average > 4:
		return 'X'
	elif line[5] == 'Penta':
		deficit = 5 - average
		needed = deficit * length
		boxes = needed / 2
		boxes = round(boxes * 2) / 2 
		str_boxes = str(boxes)
		if boxes == 0.5 or boxes == 0:
			return "~ 1 box"
		elif boxes == 1:
			return "1 box"
		elif str_boxes[-1:] == '0':
			return f"{str_boxes[:-2]} boxes"
		return f"{boxes} boxes"
	elif line[5] == 'Pacific':
		deficit = 5 - average
		boxes = deficit * length
		boxes = round(boxes * 2) / 2 
		str_boxes = str(boxes)
		if boxes == 0.5 or boxes == 0:
			return "~ 1 box"
		elif boxes == 1:
			return "1 box"
		elif str_boxes[-1:] == '0':
			return f"{str_boxes[:-2]} boxes"
		return f"{boxes} boxes"

# def phone_home(phone):
# 	phone = f'({phone[2:5]}) {phone[5:8]}-{phone[8:]}'
# 	# print(phone)
# 	for log in logs_:
# 		if log[8] == phone:
# 			return log

# V: {'PFA', 'SHA', 'JAV', 'SKY', 'OAL', 'FBS', 'GII', 'LAI'}
# H: {'KFDK', 'CYWG', 'CYXE', 'CYHZ', 'KFMN', 'KHLN', 'KDRO', 'KMRT', 'KRIL', 'KLYH', 'PHJR (JRF)', 'KPLU', 'KDPA', 'KRBW', 'CYLW', 'KHEF', 'KIDA', 'KCXY', 'KBJC', 'KHDC', 'KMGY', 'KCRG', 'KHKY', 'KSNY', 'KSTC', 'KRDM', 'KGKY', 'KDLH', 'KPIH', 'KAVP', 'CYXC', 'KJAN', 'KJKJ', 'KBKV', 'KLNK', 'KCMI', 'KCOE', 'KMAF', 'KOLM', 'KAEG', 'KROC', 'CYQY', 'KTVC', 'KBFF', 'KSGU', 'KPVU', 'PHKO (KOA)', 'KSXK', 'KSBN', 'KYKM', 'KRNO', 'KRME', 'KGTU', 'KFNL', 'CZVL', 'KFCM', 'PHOG (OGG)'}
# R: {'C6', 'GE300', '65 Twister', 'N5', 'GE220', 'N5IR', 'HubbleIR', 'Hubble'}