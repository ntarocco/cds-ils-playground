import click
from flask.cli import with_appcontext

from invenio_db import db
from invenio_indexer.api import RecordIndexer
from invenio_pidstore.models import PersistentIdentifier
from invenio_records.api import Record

from ilsplayground.api import BookRecord, ItemRecord, LocationRecord
from ilsplayground.pid.minters import book_pid_minter, item_pid_minter, \
    location_pid_minter
from ilsplayground.pid.fetchers import book_pid_fetcher, item_pid_fetcher, \
    location_pid_fetcher


LOCATIONS = [
    {
        # PID 1
        "name": "CERN Library",
        "address": "Building 52-1-052"
    }
]

BOOKS = [
    {
        # PID 2
        "title": "The Gulf: The Making of An American Sea",
        "authors": "Jack E. Davis",
        "description": "",
    },
    {
        # PID 3
        "title": "Prairie Fires: The American Dreams of Laura Ingalls Wilder",
        "authors": "Caroline Fraser",
        "description": "",
    },
    {
        # PID 4
        "title": "Half-light: Collected Poems 1965-2016",
        "authors": "Frank Bidart",
        "description": "",
    },
    {
        # PID 5
        "title": "Locking Up Our Own: Crime and Punishment in Black America",
        "authors": "James Forman Jr.",
        "description": "",
    },
    {
        # PID 6
        "title": "Less: A Novel",
        "authors": "Andrew Sean Greer",
        "description": "",
    }
]

ITEMS = [
    {
        "title": "The Gulf: The Making of An American Sea - Item 1",
        "book_pid": "2",
        "location_pid": "1"
    },
    {
        "title": "The Gulf: The Making of An American Sea - Item 2",
        "book_pid": "2",
        "location_pid": "1"
    },
    {
        "title": "Prairie Fires: The American Dreams of Laura Ingalls Wilder",
        "book_pid": "4",
        "location_pid": "1"
    },
    {
        "title": "Half-light: Collected Poems 1965-2016",
        "book_pid": "4",
        "location_pid": "1"
    },
    {
        "title": "Half-light: Collected Poems 1965-2016",
        "book_pid": "4",
        "location_pid": "1"
    },
    {
        "title": "Half-light: Collected Poems 1965-2016",
        "book_pid": "4",
        "location_pid": "1"
    },
    {
        "title": "Less: A Novel",
        "book_pid": "6",
        "location_pid": "1"
    },
    {
        "title": "Less: A Novel",
        "book_pid": "6",
        "location_pid": "1"
    },
    {
        "title": "Less: A Novel",
        "book_pid": "6",
        "location_pid": "1"
    },
    {
        "title": "Less: A Novel",
        "book_pid": "6",
        "location_pid": "1"
    }
]


@click.group()
def ils():
    """."""


@ils.command()
@with_appcontext
def demo():
    """."""
    indexer = RecordIndexer()

    for location in LOCATIONS:
        record = LocationRecord.create(location)
        location_pid_minter(record.id, record)
        record.commit()
        db.session.commit()
        indexer.index(record)

    for book in BOOKS:
        record = BookRecord.create(book)
        book_pid_minter(record.id, record)
        record.commit()
        db.session.commit()
        indexer.index(record)

    for item in ITEMS:
        record = ItemRecord.create(item)
        item_pid_minter(record.id, record)
        record.commit()
        db.session.commit()
        indexer.index(record)
