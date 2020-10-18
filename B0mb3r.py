from twilio.rest import Client

account_sid = 'AC03705d2804ae2479f92c49220a5629ef'
auth_token = 'a854428c0c2dd64fadca84dd67de73ab'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=open("bee.txt")
    to='whatsapp:+252633630649'
)

print(message.sid)
