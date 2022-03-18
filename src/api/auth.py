from flask_restful import Resource, abort
from flask_restful.reqparse import RequestParser
from werkzeug.security import generate_password_hash, check_password_hash

from api.utils import ResCode
from db.member import member_exists, get_member_hashword, insert_member, update_member_session


class SignUp(Resource):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('user', type=str, dest='username', required=True,
                                 help='A username is required to signup.')
        self.parser.add_argument('pass', type=str, dest='password', required=True,
                                 help='A password is required to signup.')
        self.parser.add_argument('first', type=str, dest='first_name', required=True,
                                 help='A first name is required to signup.')
        self.parser.add_argument('last', type=str, dest='last_name', required=True,
                                 help='A last name is required to signup.')
        self.parser.add_argument('email', type=str, required=True, help='An email is required to signup.')

    def post(self):
        args = self.parser.parse_args()

        # Hash password
        args['password'] = generate_password_hash(args['password'], method='sha512')

        if not member_exists(email=args['email']):
            insert_member(**args)
        else:
            abort(ResCode.CONFLICT.value, message='A user with that email already exists')

        return '', ResCode.CREATED.value


class Login(Resource):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('email', type=str, required=True, help='A username is needed to login.')
        self.parser.add_argument('pass', type=str, dest='password', required=True,
                                 help='A password is needed to login.')

    def post(self):
        from secrets import token_urlsafe
        from datetime import datetime, timedelta

        args = self.parser.parse_args()

        hashword = get_member_hashword(args['email'])['password']
        password = args['password']

        if not member_exists(email=args['email']) or not check_password_hash(hashword, password):
            return {'message': 'Please check your login details and try again'}, ResCode.NOT_FOUND.value

        session_data = {'session_key': token_urlsafe(),
                        'session_expire': str(datetime.today() + timedelta(days=2))}

        update_member_session(args['email'], session_data['session_key'], session_data['session_expire'])

        return session_data, ResCode.CREATED.value


class Logout(Resource):
    @staticmethod
    def post(member_id):
        return {'message': 'Successfully logged out'}, ResCode.SUCCESS.value
