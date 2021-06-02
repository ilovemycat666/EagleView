# This is doing nothing. Functionality has been moved into app.py 


from slack_sdk.webhook import WebhookClient
url = "https://hooks.slack.com/services/your specific address here"
webhook = WebhookClient(url)

message = "Another"

response = webhook.send(text=message)
assert response.status_code == 200
assert response.body == "ok"


