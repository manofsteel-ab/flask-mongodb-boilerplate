from app.commons.models.base import Base
from app.settings.extensions import db


class Sample(Base):
    name = db.StringField(db_field='name', required=True, null=False)
    type = db.StringField(
        db_field='type', choices=[
            "sample_one", "sample_one_two"
        ]
    )

    @classmethod
    def get_by_name(cls, name):
        return cls.objects(name=name)
