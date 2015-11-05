# Download the twilio-python library from http://twilio.com/docs/libraries
#https://www.twilio.com/docs/quickstart/python/sms for more info
# sending sms
from twilio.rest import TwilioRestClient
import os  # not needed

# Find these values at https://twilio.com/user/account
#this is an option if you dont have your passwords stored
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]
# client = TwilioRestClient(account_sid, auth_token)

#all you because Magic
client = TwilioRestClient()


# #sending 1 person a text and/or a photo:
# message = client.messages.create(to=#"+friendnumber", from_=#"+twilionumber" ,
                                 # body="Hello friends!",
                                 # media_url='http://cdn.hellogiggles.com/wp-content/uploads/2015/03/15/hey-girl-is.jpg')

# #Sending it to more than 1 person
friends = ['friends numbers']
for friend in friends:
    message = client.messages.create(to=friend, from_="+17146811922",
                                     body="Hey gurlll!",
                                     media_url=['http://cdn.hellogiggles.com/wp-content/uploads/2015/03/15/hey-girl-is.jpg'])
