from flask_restful import Resource, abort
from flask_restful.reqparse import RequestParser

from api.utils import ResCode
from db.member import fetch_all_members, fetch_member, insert_member, update_member, delete_member, member_exists


class Member(Resource):
    @staticmethod
    def get(member_id):
        Member.resource_exists(member_id)
        return fetch_member(member_id), ResCode.SUCCESS.value

    @staticmethod
    def put(member_id, *args, **kwargs):
        # TODO: Implement and test
        print(args, kwargs)

        update_member(member_id, **kwargs)
        return '', ResCode.NO_CONTENT.value

    @staticmethod
    def delete(member_id):
        Member.resource_exists(member_id)
        delete_member(member_id)
        return '', ResCode.NO_CONTENT.value

    @staticmethod
    # TODO: Turn into wrapper func
    def resource_exists(member_id):
        if not member_exists(member_id):
            abort(ResCode.NOT_FOUND.value, message=f'No member exists with id {member_id}')


class MemberList(Resource):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('last', type=str, required=True, help='A member needs a last name')
        self.parser.add_argument('first', type=str, required=True, help='A member needs a first name')
        self.parser.add_argument('user', type=str, required=True, help='A member needs a username')
        self.parser.add_argument('email', type=str, required=True, help='A member needs an email')

    @staticmethod
    def get():
        return fetch_all_members()

    # TODO: Implement and test
    def post(self):
        args = self.parser.parse_args()

        insert_member(**args)

        return '', ResCode.CREATED.value
