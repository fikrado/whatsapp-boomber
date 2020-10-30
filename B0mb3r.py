
# remember you need twilo acount and cloud app




from twilio.rest import Client 
 
account_sid = '(acount id)' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='your no ',  
                              body=open("/bee.txt",      
                              to='whatsapp:victam no' 
                          ) 
 
print(message.sid)
