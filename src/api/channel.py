import json

from flask_restful import Resource

from src.api.utils import DatetimeEncoder
from src.db.channel import fetch_all_channels
from src.db.message import fetch_all_msgs_from_chan


class Channel(Resource):
    @staticmethod
    def get(id=None):
        if id:
            return json.dumps(fetch_all_msgs_from_chan(chan_id=id), cls=DatetimeEncoder, separators=(',', ':'),
                              sort_keys=True)
        else:
            return fetch_all_channels()
