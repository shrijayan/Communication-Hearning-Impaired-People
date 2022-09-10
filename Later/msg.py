from twilio.rest import Client 
account_sid = 'AC7879cd351441a3e37b56f517d052de2b' 
auth_token = 'ea18149bdae6f9dd106293078647cba1' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+916379440984' 
                          ) 
 
print(message.sid)
