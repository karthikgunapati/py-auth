import twilio
from twilio.rest import Client


class twilioSMSUtil(object):
    def __init__(self, sid, token, fromNumber, toNumber):
        self.client = Client(sid, token)
        self.fromNumber = fromNumber
        self.toNumber = toNumber
    

    def send_sms(self, message, **kwargs):
        """
        this function returns the following body
        {
        "account_sid":  "XXXXXXX",
        "api_version":  "XXXXXXX",
        "body":  "XXXXXXX",
        "date_created": "XXXXXXX",
        "date_sent":  "XXXXXXX",
        "date_updated":  "XXXXXXX",
        "direction":  "XXXXXXX",
        "error_code": null,
        "error_message": null,
        "from":  "XXXXXXX",
        "messaging_service_sid":  "XXXXXXX",
        "num_media":  "XXXXXXX",
        "num_segments":  "XXXXXXX",
        "price":  XXXXXXX,
        "price_unit":  "XXXXXXX",
        "sid":  "XXXXXXX",
        "status":  "XXXXXXX",
        "subresource_uris": {
        "media": "XXXXXXX"
        }
        """
        msg = self.client.messages.create(body=message.format(**kwargs), from_= self.fromNumber, to=self.toNumber)
        return msg.sid
