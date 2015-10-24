from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC38b690c158eee466fea8748f957b8bc1"
auth_token = "09c1eb561ee7c11767421f9893deca1b"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Where are Unathi's home girls?",
                                 to="+13102546839",
                                 from_="+14804183140")
print(message.sid)
