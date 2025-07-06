from flask import Flask, jsonify
app = Flask(__name__)

valid_keys = ["9TH094GIG13XX19S", "A1B2C3D4E5F6", "XYZ987654321"]

@app.route('/validkeys', methods=['GET'])
def get_keys():
    return jsonify({"keys": valid_keys})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Port 10000 is safe on Render
