from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

def generate_key(length=16):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route("/generatekey", methods=["GET"])
def generate_key_route():
    key = generate_key()
    return jsonify({"key": key})

if __name__ == "__main__":
    app.run()
