 from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC36f289a94ed85d6b85d3460bdee4a6c3" 
AUTH_TOKEN = "d0e6f70a7b2027203341d3aada11f38c" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(    
) 
