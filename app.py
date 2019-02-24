from datetime import timedelta
from flask import Flask
from flask_restful import Api
from mongoengine import connect
from flask_jwt import JWT
from utils.jwt_util import authenticate, identity
from resources.user_resources import *
from conf import *

app = Flask(__name__)
connect(dataBaseName, host=dataBaseHost, port=databasePort)
app.config['SECRET_KEY'] = secretKey
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=tokenExpirationTimeInHours)
api = Api(app, catch_all_404s=True)
jwt = JWT(app, authenticate, identity)

# routes
api.add_resource(Register, '/register')
api.add_resource(emailOTP, '/emailOTP')
api.add_resource(emailURI, '/emailURI')
api.add_resource(smsOTP, '/smsOTP')
api.add_resource(smsURI, '/smsURI')
api.add_resource(verifyUser, '/verify', '/verify/<urlsafe>')
api.add_resource(userDetails, '/user')


if __name__=='__main__':
    app.run(debug=True)