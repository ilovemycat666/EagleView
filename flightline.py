import datetime
import os
import shutil
import requests
import csv
import xlwings as xw
from xlwings.constants import DeleteShiftDirection
from collections import Counter
import operator

today = datetime.date.today()
folder_name = str(today)
folder_name = folder_name[2:4] + folder_name[5:7] + folder_name[8:]
parent_directory = 'hidden for hithub'
path = os.path.join(parent_directory, folder_name)
os.mkdir(path)
print(f"Directory {folder_name} created")

y = today - datetime.timedelta(days=1)
y = str(y)
y = y[:4] + y[5:7] + y[8:]

from_path = 'from path hidden'
to_path = 'to path hidden'
print(f"Received_Plans.csv copied to {folder_name}")

shutil.copyfile(from_path, to_path)
received_plans = []
with open('path hidden', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        received_plans.append(row)
    received_plans.pop(0)
r_len = len(received_plans)

url = 'https://eagleview.quickbase.com/db/[hidden url]'
r = requests.get(url)
with open('hidden path', 'wb') as f:
    f.write(r.content)
print(f"Flight_Lines.csv saved to {folder_name}")

flight_lines = []
with open('Flight_Lines.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        flight_lines.append(row)
flight_lines.pop(0)

wb = xw.Book('hidden file path')
RLAS = wb.sheets['RLAS-ISD+QB']
OUT = wb.sheets['Outliers']
QB = wb.sheets['QB Report']
wb2 = xw.Book('hidden file path')
QB_FL = wb2.sheets['Sheet1']

RLAS.range("A2").value = received_plans
QB.range("A2").value = flight_lines

print(f'{r_len} bottles of beer on the wall...')
for i in range(r_len):
    RLAS.range(f'H{i+2}').value = f"=VLOOKUP(B{i+2},Table2,3,FALSE)"
    RLAS.range(f'I{i+2}').value = f"=VLOOKUP(B{i+2},Table2,2,FALSE)"
    if i % 100 == 0:
        print(f'{i} bottles of beer downed')

colAK = RLAS.range(f'A2:K{r_len}').value
num = 0
for row in colAK:
    num += 1
    if row[-1] == 'DELETE ROW':
        print(f"Removed from RLAS for 'Delete Row'\n{row}")
        RLAS.range(f'{num}:{num}').api.Delete(DeleteShiftDirection.xlShiftUp)
        r_len -= 1
        num -= 1
# VOODOOMAGIK
colD = RLAS.range(f'D2:D{r_len}').value
colB_dict = Counter(colD)
num = 0
dupes = []
for k,v in colB_dict.items():
    num += 1
    if v >= 2:
        num += 1
        dupes.append([num, k, RLAS.range(f"H{num}").value, v])
        num += v - 2
dupe_troop = []
for dupe in dupes:
    group = []
    for i in range(dupe[3]):
        group.append([dupe[0]+i,
                    RLAS.range(f"D{dupe[0]+i}").value,
                    RLAS.range(f"H{dupe[0]+i}").value,
                    dupe[3],
                    RLAS.range(f"E{dupe[0]+i}").value])
    dupe_troop.append(group)
for d in dupe_troop:
    d.sort(key=operator.itemgetter(4), reverse=True)

num = 0
for troop in dupe_troop:
    # print(troop)
    dupe_group = []
    for dupe in troop:
        dupe_group.append(dupe[2])
    # print(dupe_group)
    x = None in dupe_group and any(dupe_group)
    if x == True:
        # print("Has good and bad look ups")
        for dupe in troop:
            if dupe[2] == None:
                # print(f'Remove: {dupe[0] - num}')
                print(f"Removed from RLAS for bad look up\n{dupe}")
                RLAS.range(f'{dupe[0] - num}:{dupe[0] - num}').api.Delete(DeleteShiftDirection.xlShiftUp)
                r_len -= 1
                num += 1
    elif x == False:
        # print("Has uniform look up status")
        for i in range(len(troop)):
            if i == 0:
                continue
            # print(f'Remove: {troop[i][0] - num}')
            print(f"Removed from RLAS for fewer completions\n{troop[i]}")
            RLAS.range(f'{troop[i][0] - num}:{troop[i][0] - num}').api.Delete(DeleteShiftDirection.xlShiftUp)
            r_len -= 1
            num += 1
    print('----------')
print('--------------------------------------')

r_len += 1
colAH = RLAS.range(f'A2:H{r_len}').value

outliers = []
num = 1
for row in colAH:
    num += 1
    x = None in row and any(row)
    if x:
        row = row[:-1]
        outliers.append(row)
        print(f"Removed from RLAS, added to Outliers\n{row}")
        RLAS.range(f'{num}:{num}').api.Delete(DeleteShiftDirection.xlShiftUp)
        r_len -= 1
        num -= 1
OUT.range('A2').value = outliers

o_len = len(outliers)
for i in range(o_len):
    RLAS.range(f'H{i+2}').value = f"=VLOOKUP(D{i+2},'QB Report'!B:C,2,FALSE)"

o_len += 1
colAK = OUT.range(f'A2:K{o_len}').value
num = 1
for row in colAK:
    num += 1
    if row[-1] == 'DELETE ROW':
        print(f"Deleted from Outliers for 'Delete Row':\n{row}")
        OUT.range(f'{num}:{num}').api.Delete(DeleteShiftDirection.xlShiftUp)
        num -= 1
        o_len -= 1
    elif row[7] == None:
        print(f"Deleted from Outliers for Col H == None:\n{row}")
        OUT.range(f'{num}:{num}').api.Delete(DeleteShiftDirection.xlShiftUp)
        num -= 1
        o_len -= 1


colH = RLAS.range(f'H2:L{r_len}').value
out_colH = OUT.range(f'H2:L{o_len}').value

print(f'r_len Length: {r_len}')
print(f'o_len Length: {o_len}')

QB_FL.range('A2').value = colH
QB_FL.range(f'A{r_len + 1}').value = out_colH


wb.save('hidden file path')
wb2.save('hidden file path')
# wb.close()
# wb2.close()
