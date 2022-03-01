from flask_restful import Resource

from src.db.community import fetch_all_communities


class Community(Resource):
    @staticmethod
    def get():
        return fetch_all_communities()
