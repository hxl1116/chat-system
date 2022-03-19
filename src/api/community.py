from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from api.base import Base
from api.utils import ResCode
from db.channel import fetch_all_channels
from db.community import fetch_all_communities


class Community(Resource, Base):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('Session-Key', type=str, dest='session_key', location='headers', required=True,
                                 help='You need to be logged in to do this action.')
        self.parser.add_argument('member', type=str, location='headers', required=True,
                                 help='A member\'s username is needed for this action.')

    def get(self):
        args = self.parser.parse_args()

        self.authorize(args)

        communities = fetch_all_communities()
        channels = fetch_all_channels()

        for comm in communities:
            comm['channels'] = []
            for chan in channels:
                if comm['community_id'] == chan['community_id']:
                    comm['channels'] = comm['channels'] + [chan]

        return communities, ResCode.SUCCESS.value
