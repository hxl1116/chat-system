from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from werkzeug.security import generate_password_hash, check_password_hash

from api.utils import ResCode
from db.member import member_exists, get_member_hashword


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

    @staticmethod
    def get():
        return 'Sign Up', ResCode.SUCCESS

    # TODO: Refactor to use SQLAlchemy
    def post(self):
        args = self.parser.parse_args()

        # Hash password
        args['pass'] = generate_password_hash(args['pass'], method='sha256')

        # if member_exists(email=args['email']):
        #     insert_member(**args)
        # else:
        #     abort(ResCode.CONFLICT, message='A user with that email already exists')

        return '', ResCode.CREATED


class Login(Resource):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('email', type=str, required=True, help='A username is needed to login.')
        self.parser.add_argument('pass', type=str, dest='password', required=True,
                                 help='A password is needed to login.')

    @staticmethod
    def get():
        return 'Login', ResCode.SUCCESS

    def post(self):
        args = self.parser.parse_args()

        if not member_exists(email=args['email']) or not check_password_hash(args['pass'],
                                                                             get_member_hashword(args['email'])):
            return {'message': 'Please check your login details and try again'}, ResCode.NOT_FOUND

        return {'message': 'Successfully logged in'}, ResCode.SUCCESS


class Logout(Resource):
    @staticmethod
    def post(member_id):
        return {'message': 'Successfully logged out'}, ResCode.SUCCESS
