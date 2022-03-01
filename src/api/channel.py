from flask_restful import Resource

from src.db.channel import fetch_all_channels
from src.db.message import fetch_all_msgs_from_chan


class Channel(Resource):
    @staticmethod
    def get(id=None):
        if id:
            # FIXME: 'datetime' not JSON serializable
            return fetch_all_msgs_from_chan(chan_id=id)
        else:
            return fetch_all_channels()
