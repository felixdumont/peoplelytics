from twilio.rest import Client
import private_settings

# Your Account SID from twilio.com/console
account_sid = private_settings.twilio_sid
# Your Auth Token from twilio.com/console
auth_token  = private_settings.twilio_key

def send_sms(driver):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=private_settings.twilio_to_phone,
        from_=private_settings.twilio_from_phone,
        body="Hi Driver number {}. You are entering a high risk zone. Please be careful and lower your speed.".format(
            driver))
