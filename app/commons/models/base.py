from app.settings.extensions import db


class Base(db.Document):
    meta = {'abstract': True}
    deleted = db.BooleanField(
        db_field='isDeleted', required=True, default=False, null=False
    )

    def __str__(self):
        return '{}:id:{}'.format(self.__class__.__name__, self.id)

    def __repr__(self):
        return self.__str__()

    @db.queryset_manager
    def objects(cls, queryset):
        return queryset.filter(deleted=False)

    @classmethod
    def add(cls, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def assign_attributes(self, data):
        pass

    def to_dict(self):
        response = {}
        return response
