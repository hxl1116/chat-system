from flask_restful import Resource

from src.api.utils import ResCode
from src.db.message import fetch_all_msgs_from_chan


class Channel(Resource):
    @staticmethod
    def get(chan_id):
        # TODO: Check if channel exists

        return [[*msg[0:-1], msg[-1].strftime('%Y-%m-%d %H:%M:%S.%f %z')]
                for msg in fetch_all_msgs_from_chan(chan_id=chan_id)], ResCode.SUCCESS.value


class ChannelList(Resource):
    @staticmethod
    def get():
        from src.db.models.channel import Channel

        return [row.format() for row in Channel.fetch_all()], ResCode.SUCCESS.value
