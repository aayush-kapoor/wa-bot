from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    msg=msg.lower()
    counter = 0
    if msg == "no" or msg == "nope" or msg == "nah" or msg == "n" or msg == "not yet":
        resp = MessagingResponse()
        resp.message("A missing pill can cause a break in your treatment, don’t miss your pill!")
        counter = 1 

if __name__ == "__main__":
    app.run(debug=True)
