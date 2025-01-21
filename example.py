import requests




def send_test_message():
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "channel": SLACK_CHANNEL,
        "text": "Test message from Honey Token system."
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Failed with status code:", response.status_code, response.text)

# Run the test
send_test_message()
