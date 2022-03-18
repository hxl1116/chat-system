from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from src.server import db


class Message(db.Model):
    msg_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    chan_id = db.Column(UUID(as_uuid=True))
    sender_id = db.Column(UUID(as_uuid=True))
    content = db.Column(db.String(10000))
    timestamp = db.Column(db.DateTime)
