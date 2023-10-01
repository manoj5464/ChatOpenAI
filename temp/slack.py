import os
from slack_sdk import WebClient

# Initialize a Slack WebClient with your OAuth token
slack_token = "xoxe.xoxp-1-Mi0yLTg1MzMwMzU5NTMyOC0zODkzOTI1NzY1NTkxLTU5OTgwMTQ0NzAwNjQtNTk3NDkyMjc2MTM5NS1mYjU1MTczNjNiNjQyODljYjYyODA1NTBiMmI5YTcxZTJjMTI4MDQxYzk1N2JhZTE4ZGY3MzE3NDM2YzJlNzhm" #os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

# Specify the channel ID or name of the channel you want to retrieve messages from
channel_id = "bookstore-research-error-log-mail"

# Call the conversations.history API to get messages from the channel
response = client.conversations_history(channel=channel_id)

# Check if the API call was successful
if response["ok"]:
    messages = response["messages"]
    for message in messages:
        print(message)
else:
    print(f"Error: {response['error']}")

