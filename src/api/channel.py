from flask_restful import Resource

from db.channel import fetch_all_channels
from db.message import fetch_all_msgs_from_chan


class Channel(Resource):
    @staticmethod
    def get(id=None):
        if id:
            res = []

            for msg in fetch_all_msgs_from_chan(chan_id=id):
                res.append([*msg[0:-1], msg[-1].strftime('%Y-%m-%d %H:%M:%S.%f %z')])

            return res
        else:
            return fetch_all_channels()
