from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from server import db


class Channel(db.Model):
    channel_id = db.Column(UUID(), primary_key=True, default=uuid4)
    community_id = db.Column(UUID())
    channel_name = db.Column(db.String(1000))

    @staticmethod
    def fetch_all():
        return Channel.query.all()

    @staticmethod
    def fetch_one(id):
        return Channel.query.filter(channel_id=id).first()

    def format(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
