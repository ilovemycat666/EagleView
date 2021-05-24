# This is doing nothing. Functionality has been moved into app.py 


from slack_sdk.webhook import WebhookClient
url = "https://hooks.slack.com/services/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"
webhook = WebhookClient(url)

message = "Another"

response = webhook.send(text=message)
assert response.status_code == 200
assert response.body == "ok"



# richer text
# webhook = WebhookClient(url)
# response = webhook.send(
#     text="fallback",
#     blocks=[
#         {
#             "type": "section",
#             "text": {
#                 "type": "mrkdwn",
#                 "text": "You have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*"
#             }
#         }
#     ]
# )