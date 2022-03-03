from db.member import fetch_all_members
from flask_restful import Resource


class Member(Resource):
    @staticmethod
    def get():
        return fetch_all_members()
