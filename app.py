from flask import Flask, render_template, request, session
from flask_ngrok import run_with_ngrok
from daily_logs import pull_logs
from twilio.twiml.messaging_response import MessagingResponse
from slack_sdk.webhook import WebhookClient

app = Flask(__name__)
run_with_ngrok(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 5

# # url = "https://hooks.slack.com/services/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" # Pilot Logs Test URL
# url = "https://hooks.slack.com/services/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" # TC Shipping Channel
# webhook = WebhookClient(url)

pull_logs = pull_logs()

@app.route('/')
def index():
    return render_template('index.html', drive_count=pull_logs[1], canadian=pull_logs[3], hangars=pull_logs[4])

# @app.route('/sms', methods=['GET','POST'])
# def sms_reply():
# 	if request.method == 'GET':
# 		return render_template('sms.html')
# 	elif request.method == 'POST':
# 	    # Respond to incoming calls with a simple text message.
# 	    # Start our TwiML response
# 	    resp = MessagingResponse()
# 	    # Add a message
# 	    resp.message("Thanks for getting back to us.")
# 	    phone = request.values.get('From')

# 	    # message to slack
# 	    log = phone_home(phone)
# 	    print(f"LOG: {log}")

# 	    if log == None:
# 	    	print("No Phone Number Match")
# 	    	response = webhook.send(text=f"Phone number: {phone} not recognized")
# 	    	return str(resp)
# 	    body = request.values.get('Body')
# 	    slack_message = f"{log[7]} has responded: {body}. Contact him at {log[8]}"
# 	    response = webhook.send(text=slack_message)
# 	    assert response.status_code == 200
# 	    assert response.body == "ok"

# 	    return str(resp)

# @app.route('/slack', methods=['GET','POST'])
# def receive_slack():
# 	if request.method == 'GET':
# 		return 'Get Request'
# 	elif request.method == 'POST':
# 		...
   


if __name__ == "__main__":
    app.run()




# gets all post details
# print(dict(request.values.items()))	
# {'ToCountry': 'US', 
# 'ToState': 'CA', 
# 'SmsMessageSid': 'SM24d05b3dad306825a037f8c8d0c92331', 
# 'NumMedia': '0', 
# 'ToCity': '', 
# 'FromZip': '14623', 
# 'SmsSid': 'SM24d05b3dad306825a037f8c8d0c92331', 
# 'FromState': 'NY', 
# 'SmsStatus': 'received', 
# 'FromCity': 'ROCHESTER', 
# 'Body': 'F', 
# 'FromCountry': 'US', 
# 'To': '+14243484582', 
# 'ToZip': '', 
# 'NumSegments': '1', 
# 'MessageSid': 'SM24d05b3dad306825a037f8c8d0c92331', 
# 'AccountSid': 'AC28ce78f51dc88ba514b50112ac6b5f2d', 
# 'From': '+15857031895', 
# 'ApiVersion': '2010-04-01'}