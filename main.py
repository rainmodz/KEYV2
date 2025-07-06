from flask import Flask, render_template, redirect, url_for, jsonify
import random
import string
import json
import os

app = Flask(__name__)

def generate_key(length=16):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generatekey')
def get_key():
    new_key = generate_key()
    
    keys = []
    if os.path.exists("keys.json"):
        with open("keys.json", "r") as f:
            keys = json.load(f)
    
    keys.append(new_key)
    with open("keys.json", "w") as f:
        json.dump(keys, f)
    
    return jsonify({"key": new_key})
