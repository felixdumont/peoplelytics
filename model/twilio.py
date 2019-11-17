from twilio.rest import Client
import private_settings

# Your Account SID from twilio.com/console
account_sid = "AC840f7f0f50508da30702b3dc79bc5b83"
# Your Auth Token from twilio.com/console
auth_token  = private_settings.twilio_key

def send_sms(driver):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+18572858877",
        from_="+13343842820",
        body="Hi Driver number {}. You are entering a high risk zone. Please be careful and lower your speed.".format(
            driver))
