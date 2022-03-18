from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from src.server import db


class Community(db.Model):
    community_id = db.Column(UUID(), primary_key=True, default=uuid4)
    community_name = db.Column(db.String(1000))

    @staticmethod
    def fetch_all():
        return Community.query.all()

    def format(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
