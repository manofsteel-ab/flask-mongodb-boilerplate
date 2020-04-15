from datetime import datetime

from app.settings.extensions import db


class Base(db.Document):
    meta = {'abstract': True}
    created_at = db.DateTimeField(
        db_field='createdAt', required=True, default=datetime.utcnow()
    )
    updated_at = db.DateTimeField(
        db_field='updatedAt', required=True, default=datetime.utcnow()
    )
    deleted = db.BooleanField(
        db_field='isDeleted', required=True, default=False, null=False
    )

    default_columns = ['id', 'created_at', 'updated_at']

    def __str__(self):
        return '{}:id:{}'.format(self.__class__.__name__, self.id)

    def __repr__(self):
        return self.__str__()

    @db.queryset_manager
    def objects(cls, queryset):
        return queryset.filter(deleted=False)

    @classmethod
    def add(cls, *args, **kwargs):
        print(db)
        obj = cls()
        obj.assign_attributes(kwargs)
        print(kwargs.items())
        if kwargs.get('save'):
            print(234234)
            obj.save()
        return obj

    def update(self, *args, **kwargs):
        self.assign_attributes(kwargs)
        if save:
            self.save()
        return self

    def assign_attributes(self, data):
        for col_name, value in data.items():
            if col_name not in self.default_columns:
                if hasattr(self, col_name) and data.get(col_name) is not None:
                    setattr(self, col_name, data[col_name])
        return self

    def to_json(self):
        response = {}
        for field_name in self:
            value = getattr(self, field_name)
            if type(value) == datetime:
                response[field_name] = str(convert_iso_to_utc(value))
            elif type(value) == ObjectId:
                response[field_name] = str(value)
            elif type(value) == Decimal:
                response[field_name] = str(value)
            else:
                response[field_name] = value
        return response
