from flask_restful import Resource, abort
from flask_restful.reqparse import RequestParser

from api.utils import ResCode
from db.member import fetch_member, fetch_all_members, update_member, delete_member, member_exists, validate_session


class Base:
    @staticmethod
    def validate(id):
        # Check user exists
        if not member_exists(id=id):
            abort(ResCode.CONFLICT.value, message='A member with that id does not exist.')

    @staticmethod
    def authorize(args):
        # Check session key
        if not validate_session(user=['member'], session=args['session_key']):
            abort(ResCode.CONFLICT.value, message='A member with that username is not logged in.')


class Member(Resource, Base):
    def __init__(self):
        self.base_parser = RequestParser()
        # self.base_parser.add_argument('Session-Key', type=str, dest='session_key', location='headers', required=True,
        #                               help='You need to be logged in to do this action.')
        # self.base_parser.add_argument('member', type=str, required=True,
        #                               help='A member\'s username is needed for this action.')

        self.put_parser = self.base_parser.copy()
        self.put_parser.add_argument('last', type=str, dest='last_name')
        self.put_parser.add_argument('first', type=str, dest='first_name')
        self.put_parser.add_argument('user', type=str, dest='username')
        self.put_parser.add_argument('pass', type=str, dest='password')
        self.put_parser.add_argument('email', type=str, dest='email')

    def get(self, member_id):
        # args = self.base_parser.parse_args()

        self.validate(member_id)
        # self.authorize(args)

        member = fetch_member(member_id)

        return member, ResCode.SUCCESS.value

    def post(self):
        pass

    def put(self, member_id):
        args = self.put_parser.parse_args()

        self.validate(member_id)
        # self.authorize(args)

        update_member(member_id, **args)

        return '', ResCode.CREATED.value

    def delete(self, member_id):
        # args = self.base_parser.parse_args()

        self.validate(member_id)
        # self.authorize(args)

        delete_member(member_id)

        return '', ResCode.NO_CONTENT.value


class MemberList(Resource, Base):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('Session-Key', type=str, dest='session_key', location='headers', required=True,
                                 help='You need to be logged in to do this action.')
        self.parser.add_argument('member', type=str, required=True,
                                 help='A member\'s username is needed for this action.')

    def get(self):
        # args = self.parser.parse_args()

        # self.authorize(args)

        # Get all members from the db
        members = fetch_all_members()

        # Cast 'username_changed_date' field to 'str' type for each record
        members = [{**member, 'username_changed_date': str(member['username_changed_date'])} for member in members]

        return members, ResCode.SUCCESS.value
