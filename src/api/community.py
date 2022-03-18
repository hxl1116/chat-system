from flask_restful import Resource

from api.utils import ResCode

from db.channel import fetch_all_channels
from db.community import fetch_all_communities


class Community(Resource):
    @staticmethod
    def get():
        communities = fetch_all_communities()
        channels = fetch_all_channels()

        for comm in communities:
            comm['channels'] = []
            for chan in channels:
                if comm['community_id'] == chan['community_id']:
                    comm['channels'] = comm['channels'] + [chan]

        return communities, ResCode.SUCCESS.value
