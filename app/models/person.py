from app.ext.database import db

class Persons(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    name = db.Column(db.String(255))
    rating = db.Column(db.Float)
    image_url = db.Column(db.String(255))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}