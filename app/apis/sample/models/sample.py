from app.commons.models.base import Base
from app.settings.extensions import db
class Sample(Base):
    meta = {
        'allow_inheritance': True,
        'collection': 'sample',
        'indexes': [
            'zone_id'
        ]
    }
    name = db.StringField(db_field='name', null=False)
    type = db.StringField(
        db_field='type', null=False, choices=[
            "one", "two"
        ]
    )

    @classmethod
    def get_by_name(cls, name):
        return cls.objects(zone_id=zone_id)
