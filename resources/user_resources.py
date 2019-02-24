from datetime import datetime, timedelta
from itsdangerous import URLSafeSerializer, BadSignature
from flask_restful import Resource, reqparse, abort
from flask import jsonify, request
from models.user_models import User
from utils.basic_utils import req_parser, generate_otp
from flask_jwt import jwt_required, current_identity
from resource_args.user_args import *
from conf import *
from utils.email_util import emailUtil
from utils.sms_util import twilioSMSUtil


class Register(Resource):

    def post(self):
        args = req_parser(*register_args)
        if User.objects(email_id=args['email_id']).first():
            abort(409, message="'{0}' already exists".format(args['email_id']))
        user = User(
            email_id=args['email_id'],
            first_name=args['first_name'],
            last_name=args['last_name'],
            password=args['password'],
            phone_num=args['phone_num'],
            company_name=args['company_name']
        )
        user.save()
        return jsonify({"message": "registered successfully"})


class emailOTP(Resource):
    def post(self):
        args = req_parser(*otp_generate_args)
        user = User.objects(email_id=args['user_id']).first()
        if user and user.email_id == args['user_id']:
            otp = generate_otp()
            user.update(otp=otp)
            mail = emailUtil(emailHost, subjectForOTPEmail, fromEmailForOTP, [user.email_id], emailPort, emailPassword)
            mail.send_mail(mail.message(OTPTemplate, otp=otp))
            return jsonify({"message": "success"})
        else:
            return abort(404, message="user not registered")


class emailURI(Resource):
    def post(self):
        args = req_parser(*link_generate_args)
        user = User.objects(email_id=args['user_id']).first()
        if user and user.email_id == args['user_id']:
            payload = URLSafeSerializer(secretKey).dumps(user.email_id)
            mail = emailUtil(emailHost, subjectForOTPEmail, fromEmailForOTP, [user.email_id], emailPort, emailPassword)
            mail.send_mail(mail.message(LinkTemplate, domain=request.url_root,payload=payload))
            return jsonify({"message": "success"})
        else:
            return abort(404, message="user not registered")


class userDetails(Resource):
    @jwt_required()
    def get(self):
        user = User.objects(email_id=current_identity.username).first()
        if user.verified:
            return jsonify({
                "id": user.email_id,
                "modified_date": str(user.date_modified)
            })
        else:
            return abort(401, message="please verify the account")


class smsOTP(Resource):
    def post(self):
        args = req_parser(*otp_generate_args)
        user = User.objects(email_id=args['user_id']).first()
        if user and user.email_id == args['user_id']:
            otp = generate_otp()
            user.update(otp=otp)
            sms_client = twilioSMSUtil(twilioAccountSid, twilioToken, twilioFromNumber, user.phone_num)
            return jsonify(sms_client.send_sms(OTPTemplate, otp=otp))
        else:
            abort(404)


class smsURI(Resource):
    def post(self):
        args = req_parser(*link_generate_args)
        user = User.objects(email_id=args['user_id']).first()
        if user and user.email_id == args['user_id']:
            payload = URLSafeSerializer(secretKey).dumps(user.email_id)
            sms_client = twilioSMSUtil(twilioAccountSid, twilioToken, twilioFromNumber, user.phone_num)
            return jsonify(sms_client.send_sms(LinkTemplate, domain=request.url_root, payload=payload))
        else:
            abort(404)


class verifyUser(Resource):
    def get(self, urlsafe):
        try:
            user_id = URLSafeSerializer(secretKey).loads(urlsafe)
        except BadSignature:
            abort(404)
        user = User.objects(email_id=user_id).first()
        user.update(verified=True)
        return jsonify({"message": "success"})
    
    def put(self):
        args = req_parser(*otp_verify_args)
        user = User.objects(email_id=args['user_id']).first()
        if user and user.otp == args['otp']:
            user.update(verified=True)
            return jsonify({"message": "success"})
        else:
            abort(404, message="user not found/invalid OTP")