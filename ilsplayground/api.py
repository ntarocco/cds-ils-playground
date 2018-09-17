from invenio_records.api import Record
from invenio_jsonschemas import current_jsonschemas


class BookRecord(Record):

    _schema = 'books/book-v1.0.0.json'

    @classmethod
    def create(cls, data, id_=None, **kwargs):
        data['$schema'] = current_jsonschemas.path_to_url(cls._schema)
        return super(BookRecord, cls).create(data, id_=id_, **kwargs)


class ItemRecord(Record):

    _schema = 'items/item-v1.0.0.json'

    @classmethod
    def create(cls, data, id_=None, **kwargs):
        data['$schema'] = current_jsonschemas.path_to_url(cls._schema)
        return super(ItemRecord, cls).create(data, id_=id_, **kwargs)


class LocationRecord(Record):

    _schema = 'locations/location-v1.0.0.json'

    @classmethod
    def create(cls, data, id_=None, **kwargs):
        data['$schema'] = current_jsonschemas.path_to_url(cls._schema)
        return super(LocationRecord, cls).create(data, id_=id_, **kwargs)
