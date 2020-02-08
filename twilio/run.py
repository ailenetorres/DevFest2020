# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

web_address = "http://countmein2020.online/"

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""

    msg = request.values.get("Body").lower().strip() # gets incoming message

    # Start our response
    resp = MessagingResponse()

    # Add a message
    #resp.message("Ahoy! Thanks so much for your message.")
    if (msg == "join"):
    	resp.message("Hi! Thanks for joining the Hungry Students text list!\n\n" + "Reply with 'YES' to confirm your subscription.\n\n" +
           "Check out our website to stay updated and share with your friends!\n{}".format(web_address))
    elif (msg == "yes"):
    	resp.message("You will now be able receive notifications about meal swipe requests and events with free food." + \
           "If you would like to see your swipe requests, reply with REQUESTS.\n\n")
    elif (msg == "requests"):
    	resp.message("Samantha Figueredo has requested a Ferris meal swipe at 6pm today." + \
           "If you would like to accept this request, reply with ACCEPT. If you want to deny, reply with DENY.\n\n")
    elif (msg == "accept"):
    	resp.message("You have confirmed this request. Samantha will now meet you today at Ferris at 6pm")
    elif (msg == "deny"):
    	resp.message("Meal request denied.")
    else:
    	resp.message("Please enter a valid response.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)