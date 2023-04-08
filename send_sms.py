from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACbc6db3bfac2d5077ad04a17f7fc90389"
# Your Auth Token from twilio.com/console
auth_token  = "be9dec0ca814efb1543265e5b002fc94"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919996358906", 
    from_="+15074739151",
    body="Hello This message is from Dharmbir's BackEnc")

print(message.sid)