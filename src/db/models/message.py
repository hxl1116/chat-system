from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from src.server import db


class Message(db.Model):
    message_id = db.Column(UUID(), primary_key=True, default=uuid4)
    channel_id = db.Column(UUID())
    sender_id = db.Column(UUID())
    content = db.Column(db.String(10000))
    timestamp = db.Column(db.DateTime)

    @staticmethod
    def fetch_all(chan_id=None):
        if chan_id:
            return Message.query.filter_by(channel_id=chan_id).all()
        else:
            return Message.query.all()

    def format(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
