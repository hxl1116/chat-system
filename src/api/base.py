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
