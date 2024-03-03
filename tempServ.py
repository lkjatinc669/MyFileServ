# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/')
# def check_client_device():
#     user_agent = request.headers.get('User-Agent')
#     device_type = detect_device_type(user_agent)
#     return f"Client Device Type: {device_type}"

# def detect_device_type(user_agent):
#     # Check if the user agent contains common mobile keywords
#     mobile_keywords = ['mobile', 'android', 'iphone', 'ipad']
#     return '<input type="file" id="ctrl" webkitdirectory directory multiple/>'
#     if any(keyword in user_agent.lower() for keyword in mobile_keywords):
#         pass
#     else:
#         return "PC"

# if __name__ == '__main__':
#     app.run(
#         host="0.0.0.0",
#         port=23333
#     )

import os
import json

def get_files(directory):
    files = []
    # Iterate over all entries in the directory
    for entry in os.listdir(directory):
        # Construct the full path of the entry
        full_path = os.path.join(directory, entry)
        # Check if the entry is a file
        if os.path.isfile(full_path):
            # Add the file to the list
            files.append(entry)
    return files

# Specify the directory path
directory_path = './'

# Get the list of files in the directory
files_list = get_files(directory_path)

# Convert the list of files to JSON format
files_json = json.dumps(files_list)

# Print the JSON formatted list of files
print(files_json)

import os
os.listdir()