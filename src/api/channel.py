from flask_restful import Resource

from api.utils import ResCode


class Channel(Resource):
    @staticmethod
    def get(chan_id):
        from src.db.models.message import Message
        # TODO: Check if channel exists

        msgs = [msg.format() for msg in Message.fetch_all(chan_id)]

        for msg in msgs:
            msg['timestamp'] = msg['timestamp'].strftime('%Y-%m-%d %H:%M:%S.%f %z')

        return msgs, ResCode.SUCCESS.value


class ChannelList(Resource):
    @staticmethod
    def get():
        from db.models.channel import Channel

        return [row.format() for row in Channel.fetch_all()], ResCode.SUCCESS.value
