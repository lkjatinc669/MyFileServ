from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def check_client_device():
    user_agent = request.headers.get('User-Agent')
    device_type = detect_device_type(user_agent)
    return f"Client Device Type: {device_type}"

def detect_device_type(user_agent):
    # Check if the user agent contains common mobile keywords
    mobile_keywords = ['mobile', 'android', 'iphone', 'ipad']
    return '<input type="file" id="ctrl" webkitdirectory directory multiple/>'
    if any(keyword in user_agent.lower() for keyword in mobile_keywords):
        pass
    else:
        return "PC"

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=23333
    )