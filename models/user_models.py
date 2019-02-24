from mongoengine import Document, LongField, ListField, BooleanField, EmbeddedDocument
from mongoengine import DateTimeField, StringField, EmailField, EmbeddedDocumentField
from datetime import datetime, timedelta


class trailDetails(EmbeddedDocument):
    status = BooleanField(default=False)
    valid_upto = DateTimeField()


class User(Document):
    # meta = {"allow_inheritance": True}
    email_id = EmailField(primary_key=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    password = StringField(required=True)
    phone_num = LongField(required=True)
    company_name = StringField()
    date_modified = DateTimeField(default=datetime.utcnow)
    otp = StringField()
    trail = EmbeddedDocumentField(trailDetails)
    verified = BooleanField(default=False)