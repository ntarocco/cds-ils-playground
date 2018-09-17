from invenio_search.api import RecordsSearch


class BookRecordSearch(RecordsSearch):

    class Meta:
        index = 'books'
        doc_types = None


class ItemRecordSearch(RecordsSearch):

    class Meta:
        index = 'items'
        doc_types = None


class LocationRecordSearch(RecordsSearch):

    class Meta:
        index = 'books'
        doc_types = None
