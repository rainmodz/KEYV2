from flask import Flask, render_template, redirect
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generatekey')
def generate_key():
    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return f"<h1>Your Generated Key</h1><p>{key}</p><br><p>Save this key and paste it in the script to activate.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
