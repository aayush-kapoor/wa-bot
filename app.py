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
        
    elif msg == "yes" or msg == "yaa" or msg == "yup" or msg == "y" or msg == "i have" or msg == "i wouldn't miss my pill":
        resp = MessagingResponse()
        resp.message("Great Job! I'll check back with you tomorrow.")
        counter = 2
        
    elif msg == "hi" or msg == "hey" or msg == "hello" or msg == "hey there" or msg == "good day":
        resp = MessagingResponse()
        resp.message("Hello! Have you taken your pill today? (Y/N)")
        
    elif msg == "ok" or msg == "got it" or msg == "will do":
        if counter == 1:
            resp = MessagingResponse()
            resp.message("Thank you! I'll check back with you tomorrow.")
        
        elif counter == 2:
            resp = MessagingResponse()
            resp.message("😊")
            
    else:
        resp = MessagingResponse()
        resp.message("Could you please repeat that?")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
