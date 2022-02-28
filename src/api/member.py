from flask_restful import Resource

from src.db.member import fetch_all_members


class Member(Resource):
    @staticmethod
    def get():
        return fetch_all_members()
