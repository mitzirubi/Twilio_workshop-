from flask import Flask, request, redirect
import twilio.twiml
import os

app = Flask(__name__)


# ## first simple app ##############################
# @app.route("/", methods=['GET', 'POST'])
# def hello_monkey():
#     """Respond to incoming calls with a simple text message."""

#     resp = twilio.twiml.Response()
#     #changed it from us a message and added as to send an image
#     with resp.message("Hello, Mobile Monkey") as m:
#         m.media("https://demo.twilio.com/owl.png")
#     return str(resp)
# ##################################################

#Second step building up!:

# Try adding your own number to this list!
#messaging friends hehe

#Now, when someone sends you a text message, we try to look up their name in the callers dictionary.
#If we succeed, we send them a text message with their name; otherwise, we send a text message with a generic greeting.
callers = {
    "+14182630043": "fakefriend",

}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    from_number = request.values.get('From', None)
    print request.values.get('Body', None)

    if from_number in callers:
        message = callers[from_number] + ", hey its an automated message from twilio"
        print message
    else:
        message = "Monkey, thanks for the message!"

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)
