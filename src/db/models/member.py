from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from src.server import db


class Member(db.Model):
    member_id = db.Column(UUID(), primary_key=True, default=uuid4)
    username = db.Column(db.String(1000))
    password = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    first_name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)

    @staticmethod
    def fetch_all():
        return Member.query.all()

    @staticmethod
    def fetch_one(id):
        return Member.query.filter_by(member_id=id).first()

    def format(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
