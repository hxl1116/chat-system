from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from db.member import fetch_all_members, insert_member


class Member(Resource):
    CREATED = 201

    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('last', required=True, help='Last name cannot be blank')
        self.parser.add_argument('first', required=True, help='First name cannot be blank')
        self.parser.add_argument('user', required=True, help='Username cannot be blank')
        self.parser.add_argument('email', required=True, help='Email cannot be blank')

    @staticmethod
    def get():
        return fetch_all_members()

    def post(self):
        args = self.parser.parse_args()

        return insert_member(**args), self.CREATED

    def put(self):
        return None, 201

    def delete(self):
        return '', 204
