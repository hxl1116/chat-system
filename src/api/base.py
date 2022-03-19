from flask_restful import abort

from api.utils import ResCode
from db.member import validate_session


class Base:
    @staticmethod
    def validate(id):
        pass

    @staticmethod
    def authorize(args):
        # Check session key
        if not validate_session(user=args['member'], session=args['session_key']):
            abort(ResCode.CONFLICT.value, message='A member with that username is not logged in.')

    @staticmethod
    def clean_auth(args: dict):
        # Remove session key from args
        args.pop('session_key')

        # Remove username from args
        args.pop('member')

        return args
