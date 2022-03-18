from flask_restful import Resource

from api.utils import ResCode
from db.message import fetch_all_messages
from db.channel import fetch_all_channels


class Channel(Resource):
    @staticmethod
    def get(channel_id):
        msgs = fetch_all_messages(channel_id)

        for msg in msgs:
            msg['timestamp'] = msg['timestamp'].strftime('%Y-%m-%d %H:%M:%S.%f %z')

        return msgs, ResCode.SUCCESS.value


class ChannelList(Resource):
    @staticmethod
    def get():
        channels = fetch_all_channels()

        return channels, ResCode.SUCCESS.value
