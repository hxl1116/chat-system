from flask_restful import Resource, abort
from flask_restful.reqparse import RequestParser

from api.base import Base
from api.utils import ResCode
from db.channel import channel_exists, fetch_all_channels
from db.messages.standard import fetch_all_messages


class BaseChannel(Base):
    @staticmethod
    def validate(id):
        if not channel_exists(id):
            abort(ResCode.CONFLICT.value, message='A channel with that id does not exist.')


class Channel(Resource, BaseChannel):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('Session-Key', type=str, dest='session_key', location='headers', required=True,
                                 help='You need to be logged in to do this action.')
        self.parser.add_argument('member', type=str, location='headers', required=True,
                                 help='A member\'s username is needed for this action.')

    def get(self, channel_id):
        args = self.parser.parse_args()

        self.validate(channel_id)
        self.authorize(args)

        msgs = fetch_all_messages(channel_id)

        for msg in msgs:
            msg['timestamp'] = msg['timestamp'].strftime('%Y-%m-%d %H:%M:%S.%f %z')

        return msgs, ResCode.SUCCESS.value


class ChannelList(Resource, BaseChannel):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('Session-Key', type=str, dest='session_key', location='headers', required=True,
                                 help='You need to be logged in to do this action.')
        self.parser.add_argument('member', type=str, location='headers', required=True,
                                 help='A member\'s username is needed for this action.')

    def get(self):
        args = self.parser.parse_args()

        self.authorize(args)

        channels = fetch_all_channels()

        return channels, ResCode.SUCCESS.value
