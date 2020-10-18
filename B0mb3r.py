from twilio.rest import Client 
 
account_sid = 'AC03705d2804ae2479f92c49220a5629ef' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=open("bee.txt",      
                              to='whatsapp:+252634048063' 
                          ) 
 
print(message.sid)
