from flask_restful import Resource

from db.member import fetch_all_members


class Member(Resource):
    CREATED = 201

    @staticmethod
    def get():
        return fetch_all_members()

    def post(self, last, first, user, email, user_change_date):
        return None, self.CREATED
