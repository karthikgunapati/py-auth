import math, random
from flask_restful import reqparse


def req_parser(*args):
    parser = reqparse.RequestParser()
    for kwargs in args:
        parser.add_argument(**kwargs)
    return parser.parse_args(strict=True)

def generate_otp(key="0123456789", size=6):
    otp, length = str(), len(key)
    for _ in range(size):
        otp += key[math.floor(random.random() * length)]
    return otp