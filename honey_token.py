from flask import Flask, request, jsonify
import requests
import dotenv


app = Flask(__name__)

# Slack OAuth Access Token (replace with your own token)
SLACK_API_TOKEN =  ""# Replace with your Slack token
SLACK_CHANNEL =""

  # Replace with your Slack channel name

def send_slack_alert(message):
    """
    Sends an alert to the specified Slack channel.
    """
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "channel": SLACK_CHANNEL,
        "text": message
    }
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("Alert sent to Slack successfully.")
    else:
        print(f"Error sending alert to Slack: {response.status_code}, {response.text}")


@app.route('/api/token_trigger', methods=['POST'])
def token_trigger():
    """
    Endpoint that receives a POST request when a honey token is triggered.
    It sends an alert to Slack.
    """
    # Extract data from the request
    token_data = request.get_json()
    user_id = token_data.get("user_id")
    sensitive_area = token_data.get("sensitive_area")

    # Create the alert message
    message = f"Honey token triggered! User ID: {user_id}, Sensitive Area: {sensitive_area}"

    # Send alert to Slack
    send_slack_alert(message)

    return jsonify({"status": "success"}), 200


if __name__ == '__main__':
    # Start the Flask server
    app.run(debug=True, host='0.0.0.0', port=5000)
