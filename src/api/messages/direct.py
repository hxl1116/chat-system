from datetime import datetime

from flask_restful import Resource, abort
from flask_restful.reqparse import RequestParser

from api.base import Base
from api.utils import ResCode
from db.member import member_exists
from db.messages.direct import fetch_many_dms, insert_dm


class Direct(Resource, Base):
    def __init__(self):
        self.base_parser = RequestParser()
        self.base_parser.add_argument('Session-Key', type=str, dest='session_key', location='headers', required=True,
                                      help='You need to be logged in to do this action.')
        self.base_parser.add_argument('member', type=str, location='headers', required=True,
                                      help='A member\'s username is needed for this action.')

        self.get_parser = self.base_parser.copy()
        self.get_parser.add_argument('Limit', type=str, dest='limit', default=None)

        self.post_parser = self.base_parser.copy()
        self.post_parser.add_argument('sender', type=str, dest='sender_id', required=True)
        self.post_parser.add_argument('receiver', type=str, dest='receiver_id', required=True)
        self.post_parser.add_argument('content', type=str, required=True)

    @staticmethod
    def validate(user):
        # Check user exists
        if not member_exists(user=user):
            abort(ResCode.CONFLICT.value, message='A member with that id does not exist.')

    def get(self, username):
        args = self.get_parser.parse_args()

        self.validate(username)
        self.authorize(args)
        args = self.clean_auth(args)

        dms = fetch_many_dms(username, args['limit'])
        dms = [{**dm, 'timestamp': str(dm['timestamp'])} for dm in dms]

        return dms, ResCode.SUCCESS.value


class DirectList(Resource, Base):
    def __init__(self):
        self.base_parser = RequestParser()
        self.base_parser.add_argument('Session-Key', type=str, dest='session_key', location='headers', required=True,
                                      help='You need to be logged in to do this action.')
        self.base_parser.add_argument('member', type=str, location='headers', required=True,
                                      help='A member\'s username is needed for this action.')

        self.post_parser = self.base_parser.copy()
        self.post_parser.add_argument('sender', type=str, dest='sender_id', required=True)
        self.post_parser.add_argument('receiver', type=str, dest='receiver_id', required=True)
        self.post_parser.add_argument('content', type=str, required=True)

    @staticmethod
    def validate(id):
        # Check user exists
        if not member_exists(id=id):
            abort(ResCode.CONFLICT.value, message='A member with that id does not exist.')

    def post(self):
        args = self.post_parser.parse_args()

        # Validate sender
        self.validate(args['sender_id'])

        # Validate receiver
        self.validate(args['receiver_id'])

        self.authorize(args)

        args = self.clean_auth(args)

        args['timestamp'] = datetime.now()

        insert_dm(**args)

        return '', ResCode.CREATED.value
