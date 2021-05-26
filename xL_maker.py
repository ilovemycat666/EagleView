import xlsxwriter
from datetime import datetime
from slack_sdk.webhook import WebhookClient
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient('BOT token here (OAuth Page on Slack.com)') # Bot User OAuth TC Shipping Channel

url = "Webhook address"
webhook = WebhookClient(url)

def create(vendors, drive_count, suggested):
	# Creating Excel file 
	today = datetime.today()
	today = str(today)
	today = today[:10]

	# Create a workbook and add a worksheet.
	workbook = xlsxwriter.Workbook(f'{today}.xlsx')

	# Formats
	bold = workbook.add_format({'bold': 1})
	center = workbook.add_format({'center_across': 1})
	center.set_right(1)

	bot_bold = workbook.add_format({'bold': 1})
	bot_bold.set_bottom(1)

	bot_center = workbook.add_format({'center_across': 1})
	bot_center.set_bottom(1)
	bot_center.set_right(1)

	highlight = workbook.add_format({'bg_color': 'yellow'})

	bot_highlight = workbook.add_format({'bg_color': 'yellow'})
	bot_highlight.set_bottom(1)

	bot_border = workbook.add_format({'bottom': 1})
	left_border = workbook.add_format({'left': 1})
	right_border = workbook.add_format({'right': 1})

	sug = workbook.add_format({'right': 1})
	sug.set_bottom(1)

	for v in vendors:
		worksheet = workbook.add_worksheet(v)
		worksheet.write('A1', f'{v}', bot_bold)
		worksheet.write('J1', 'Suggested', bot_bold)
		worksheet.write('K1', 'Shipped', bot_bold)
		worksheet.set_column('H:H', 15)
		worksheet.set_column('C:C', 5)
		worksheet.set_column('I:I', 5)
		worksheet.set_landscape()
	  
		col = 0
		row = 1

		for vendor in drive_count:
			if vendor[0][0][0] == v:
				for group in vendor:
					g_count = 0
					for line in group:
						g_count += 1
						if len(group) != g_count:
							worksheet.write(row, col, line[1])
							worksheet.write(row, col + 1, line[2])
							worksheet.write(row, col + 2, line[3])
							worksheet.write(row, col + 3, line[4])
							if line[5] == 'Pacific':
								worksheet.write(row, col + 4, line[5], highlight)
							else:
								worksheet.write(row, col + 4, line[5])
							worksheet.write(row, col + 5, line[6])
							worksheet.write(row, col + 6, line[7])
							worksheet.write(row, col + 7, line[8])
							worksheet.write(row, col + 8, line[9], center)
							worksheet.write(row, col + 9, 'X', right_border)

							row += 1
						elif len(group) == g_count:
							worksheet.write(row, col, line[1], bot_border)
							worksheet.write(row, col + 1, line[2], bot_border)
							worksheet.write(row, col + 2, line[3], bot_border)
							worksheet.write(row, col + 3, line[4], bot_border)
							if line[5] == 'Pacific':
								worksheet.write(row, col + 4, line[5], bot_highlight)
							else:
								worksheet.write(row, col + 4, line[5], bot_border)
							worksheet.write(row, col + 5, line[6], bot_border)
							worksheet.write(row, col + 6, line[7], bot_border)
							worksheet.write(row, col + 7, line[8], bot_border)
							worksheet.write(row, col + 8, line[9], bot_center)
							worksheet.write(row, col + 9, suggested(len(group), line), sug)  
							worksheet.write(row, col + 10, None, bot_border)  	

							row += 1
	workbook.close()



	try:
	    filepath=f"{today}.xlsx"
	    # response = client.files_upload(channels='#pilot-spot', file=filepath)
	    response = client.files_upload(channels='#tc-shipping', file=filepath)
	    assert response["file"]  # the uploaded file
	except SlackApiError as e:
	    # You will get a SlackApiError if "ok" is False
	    assert e.response["ok"] is False
	    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
	    print(f"Got an error: {e.response['error']}")
