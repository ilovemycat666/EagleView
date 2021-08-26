from flask import Flask, render_template, request, session
from flask_ngrok import run_with_ngrok
from daily_logs import pull_logs
from twilio.twiml.messaging_response import MessagingResponse
from slack_sdk.webhook import WebhookClient

app = Flask(__name__)
run_with_ngrok(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 5


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
