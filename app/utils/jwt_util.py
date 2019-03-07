from werkzeug.security import safe_str_cmp
from models.user_models import User


class user_auth(object):
    def __init__(self, username, password):
        self.id = username
        self.username = username
        self.password = password

def authenticate(username, password):
    user = User.objects(email_id=username).first()
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user_auth(user.email_id,user.password)

def identity(payload):
    user_id = payload['identity']
    user = User.objects(email_id=user_id).first()
    return user_auth(user.email_id,user.password)