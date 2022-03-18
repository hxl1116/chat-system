from flask_restful import Resource

from src.api.utils import ResCode


class Community(Resource):
    @staticmethod
    def get():
        from src.db.models.channel import Channel
        from src.db.models.community import Community

        communities = [comm.format() for comm in Community.fetch_all()]
        channels = [chan.format() for chan in Channel.fetch_all()]

        for comm in communities:
            comm['channels'] = []
            for chan in channels:
                if comm['community_id'] == chan['community_id']:
                    comm['channels'] = comm['channels'] + [chan]

        return communities, ResCode.SUCCESS.value
