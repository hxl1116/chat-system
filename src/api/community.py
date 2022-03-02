from flask_restful import Resource

from db.channel import fetch_all_channels
from db.community import fetch_all_communities


class Community(Resource):
    @staticmethod
    def get():
        communities = [[*community, []] for community in fetch_all_communities()]
        channels = fetch_all_channels()

        res = []

        for community in communities:
            for channel in channels:
                if community[0] == channel[1]:
                    community[2].append(channel)

            res.append(community)

        return res
