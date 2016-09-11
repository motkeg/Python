from twilio.rest import TwilioRestClient


##works only on python v3.x.x 
 
def send():
    # put your own credentials here
    ACCOUNT_SID = 'ACdb12605220baae352fff37143f3399c4'
    AUTH_TOKEN = '66b4e50233bdfd798b00eefcb3f75422'

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
        to = '+972 0525736138',
        from_ = '+1 256-740-3135 ',
        body = 'YOU ARE VERY KSILL!!!',
    )
 
 
    print("massege send")   


send()    