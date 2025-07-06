from flask import Flask, render_template, jsonify
import random
import string
import os

app = Flask(__name__)

# Generate random key
def generate_key(length=16):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generatekey')
def generate_key_route():
    key = generate_key()
    return key  # Just plain text key

# Bind to the port Render provides
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # default port if not on render
    app.run(host='0.0.0.0', port=port)
