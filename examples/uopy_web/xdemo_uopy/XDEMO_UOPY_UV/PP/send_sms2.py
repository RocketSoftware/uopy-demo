from twilio.rest import Client
def SendSMS(tophones, msgtext):

# Your Account SID from twilio.com/console
    account_sid = "AC7ddc935e841cea2eddf7978646215df4"
# Your Auth Token from twilio.com/console
    auth_token  = "006a3f2569a9f5fb0d783493b1c9847d"

    output=tophones
    output_list = output.split(',')
    for item in output_list:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        to=item,
        from_="+12564826752",
        body=msgtext)

        print(message.sid)
