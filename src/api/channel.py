from flask_restful import Resource

from api.utils import ResCode
from db.channel import fetch_all_channels
from db.message import fetch_all_msgs_from_chan


class Channel(Resource):
    @staticmethod
    def get(channel_id):
        # TODO: Check if channel exists

        return [[*msg[0:-1], msg[-1].strftime('%Y-%m-%d %H:%M:%S.%f %z')]
                for msg in fetch_all_msgs_from_chan(chan_id=channel_id)], ResCode.SUCCESS.value


class ChannelList(Resource):
    @staticmethod
    def get():
        return fetch_all_channels(), ResCode.SUCCESS.value
