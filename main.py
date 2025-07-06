from flask import Flask
import random
import string
import os

app = Flask(__name__)

# Function to generate a random key
def generate_key(length=16):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

@app.route("/")
def home():
    return "Key Generator is running."

@app.route("/generatekey")
def key():
    return generate_key()

# Required by Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use PORT env or default to 10000
    app.run(host="0.0.0.0", port=port)
