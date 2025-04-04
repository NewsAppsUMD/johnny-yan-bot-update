import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from fetch_articles import fetch_articles

# Get the Slack token from environment variables
# Initialize the Slack client with your Bot Token
client = WebClient(token=slack_token)

def generate_slack_messages():
    articles = fetch_articles()

    for article in articles:
        title = article["title"]
        link = article["link"]
        authors = article["authors"]
        pub_date = article["publication_date"]

        # Format the message using Markdown
        slack_message = (
            f"*<{link}|{title}>*\n"
            f":memo: *Authors:* {authors}\n"
            f":calendar: *Publication Date:* {pub_date}\n"
            f":link: *Read More:* <{link}>\n"
        )

        try:
            # Send the message to the Slack channel
            response = client.chat_postMessage(
                channel='slack-bots',  # Replace with your channel name
                text=slack_message
            )
            print(f"Message sent: {response['message']['text']}")
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")

if __name__ == "__main__":
    generate_slack_messages()

