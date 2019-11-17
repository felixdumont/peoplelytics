from model.train_model import train_model
from model.predict import predict

from model.twilio import send_sms

def main():
    final_model = train_model()
    predictions_df = predict(final_model)
    print(predictions_df)
    driver_alerts = set(predictions_df[predictions_df['alert'] == True]['driver_id'])
    for driver in driver_alerts:
        send_sms(driver)

#if __name__ == '__main__':
#    main()