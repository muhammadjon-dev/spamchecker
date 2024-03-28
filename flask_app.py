from flask import Flask, jsonify, request
from flask_cors import CORS
from spamfinder.spamchecker import checkspam
app = Flask(__name__)
CORS(app)



@app.route('/')
def index():
    return '<h1>Muhammad Yorqin</h1><a href="https://yorqin.com/">yorqin.com</a> '

@app.route("/spamcheck", methods=["POST"])
def spam_checker():
    data = request.get_json()
    
    if not data or "email" not in data:
        return jsonify({'error': 'Invalid input.'}), 400
    
    email = data["email"]
    
    if not email.strip():
        return jsonify({'error': 'Please enter valid mail.'}), 400
    
    result = checkspam(email)
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(debug=False)
