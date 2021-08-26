# import requests
# import csv
# from bs4 import BeautifulSoup
# from datetime import datetime
#
#
#
#
# r = requests.get('hidden url')
# sauce = BeautifulSoup(r.text, "html.parser")
# trs = sauce.find_all('tr')
# rows = []
# for tr in trs:
#     class_ = tr.get('class')
#     # print(class_)
#     if class_ == ['ev'] or class_ == ['od']:
#         rows.append(tr)
# plan_time = []
# for r in rows:
#     text = r.get_text().split("\n")
#     text = text[1:]
#     date = text[0]
#     year = date[6:]
#     date = year + '-' + date[:5]
#     date = date.split('-')
#     date = [int(d) for d in date]
#     d = datetime(date[0],date[1],date[2])
#     if d.weekday() > 4:
#         print('weekend')
#
#     print(text)
#     plan_time.append([text[0], text[1]])
#
#
# r = requests.get('hidden url')
# sauce = BeautifulSoup(r.text, "html.parser")
# trs = sauce.find_all('tr')
#
# for tr in trs:
#     class_ = tr.get('class')
#     if class_ == ['ev'] or class_ == ['od']:
#         date = tr.find("td", {"class": "FirstColumn"}).get_text()
#         a = tr.find_all('a')
#         a = [i.get_text() for i in a]
#         tail = a[2]
#         name = a[3]
#         if not a[4].isnumeric():
#             plan = a[4]
#         else:
#             plan = "N/a"
#         # print(plan, name, tail)
#         for pt in plan_time:
#             if pt[1] == plan and date == pt[0][:5]:
#                 print(pt, name)
#                 break
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import os
import time
from datetime import datetime, timedelta

opts = Options()
# opts.headless = True
driver = webdriver.Firefox(options=opts)
driver.get('hidden url')
driver.implicitly_wait(10)

div = driver.find_element_by_class_name('SigninInputWrapper')
input = div.find_elements_by_tag_name('input')
username = input[0].send_keys('edwin.reik@eagleview.com')
time.sleep(.1)
password = input[1].send_keys('b0NkY_d0Ng')
button = div.find_element_by_tag_name('button')
time.sleep(.1)
button.click()
time.sleep(.1)

# today_ = datetime.now()
# today = str(today_)
# today = today[5:10] + '-' + today[:4]
#
# later_ = today_ + timedelta(days=-3)
# later = str(later_)
# later = later[5:10] + '-' + later[:4]
#
# late_ = today_ + timedelta(days=-5)
# late = str(late_)
# late = late[5:10] + '-' + late[:4]

# days = [today_, later_, late_]
# for day in days:
#     n = day.weekday()
#     if n == 0:
#         print('Monday')
#     elif n == 1:
#         print('Tuesday')
#     elif n == 2:
#         print('Wednesday')
#     elif n == 3:
#         print('Thursday')
#     elif n == 4:
#         print('Friday')
#     elif n == 5:
#         print('Saturday')
#     elif n == 6:
#         print('Sunday')
# print(today_.weekday())
# print(later_.weekday())
# print(late_.weekday())

flightline = []
for i in range(5):
    driver.get('hidden url')
    table = driver.find_element_by_id('VR_bpw3pr8nu_31')
    trs = table.find_elements_by_tag_name('tr')
    trs = trs[3:]
    for tr in trs:
        time.sleep(.05)
        tds = tr.find_elements_by_tag_name('td')
        j = [td.text for td in tds]
        if len(tds) > 2:
            # print(tds[1].text)
            a = tds[1].find_elements_by_tag_name('a')
            if a:
                j.append(a[0].get_attribute('href'))
        flightline.append(j)
    if 'Totals' in j[0]:
        break

for i in flightline:
    x = i[-1].startswith('https://eagleview.quickbase.com')
    if x:
        driver.get(i[-1])
        time.sleep(2)
        name = driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/div/div/div/div/div[3]/table/tbody/tr[2]/td[8]/div/button/span')
        i.append(name.text)
        print(i)
        print(name.text)
    if name.text == 'Klave, Kimberly':
        break


for f in flightline:
    driver.get('hidden url')
    time.sleep(2)
    input = driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/div/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/input')
    input.send_keys(f[-1])



# os.system("taskkill /IM firefox.exe /F")
