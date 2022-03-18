from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from src.server import db


class Member(db.Model):
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = db.Column(db.String(1000))
    password = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    first_name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
