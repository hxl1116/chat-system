from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from api.utils import ResCode


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

    def post(self):
        args = self.parser.parse_args()

        # TODO: Check if user exists, otherwise create a new member

        return '', ResCode.CREATED


class Login(Resource):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('user', type=str, dest='username', required=True,
                                 help='A username is needed to login.')
        self.parser.add_argument('pass', type=str, dest='password', required=True,
                                 help='A password is needed to login.')

    @staticmethod
    def get():
        return 'Login', ResCode.SUCCESS

    def post(self):
        args = self.parser.parse_args()

        # TODO: Handle session stuff

        return {'message': 'Successfully logged in'}, ResCode.SUCCESS


class Logout(Resource):
    @staticmethod
    def post(member_id):
        # TODO: Verify member session

        return {'message': 'Successfully logged out'}, ResCode.SUCCESS
