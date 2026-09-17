from datetime import datetime, timezone

from app.ext.database import db
from app.models.person import Persons


MOCK_PERSONS = [
    {"name": "Ana Silva", "rating": 1200, "image_url": "https://i.pravatar.cc/300?img=1"},
    {"name": "Bruno Costa", "rating": 1200, "image_url": "https://i.pravatar.cc/300?img=12"},
    {"name": "Carla Souza", "rating": 1200, "image_url": "https://i.pravatar.cc/300?img=5"},
    {"name": "Diego Oliveira", "rating": 1200, "image_url": "https://i.pravatar.cc/300?img=13"},
    {"name": "Elisa Martins", "rating": 1200, "image_url": "https://i.pravatar.cc/300?img=9"},
    {"name": "Felipe Lima", "rating": 1200, "image_url": "https://i.pravatar.cc/300?img=14"},
]


def seed_database():
    if Persons.query.first() is not None:
        return False

    created_at = datetime.now(timezone.utc)
    db.session.add_all(
        [Persons(created_at=created_at, **person) for person in MOCK_PERSONS]
    )
    db.session.commit()
    return True