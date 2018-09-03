# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# ilsplayground is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Default configuration for ilsplayground.

You overwrite and set instance-specific configuration by either:

- Configuration file: ``<virtualenv prefix>/var/instance/invenio.cfg``
- Environment variables: ``APP_<variable name>``
"""

from __future__ import absolute_import, print_function

from datetime import timedelta

from invenio_circulation.config import CIRCULATION_POLICIES

from ilsplayground.api import BookRecord, ItemRecord, LocationRecord
from ilsplayground.search import BookRecordSearch, ItemRecordSearch, LocationRecordSearch
from ilsplayground.circulation.utils import circulation_items_retriver, \
    circulation_document_retriver, circulation_patron_exists, \
    circulation_item_exists, circulation_item_location_retriever, \
    circulation_is_item_available


def _(x):
    """Identity function used to trigger string extraction."""
    return x


# Rate limiting
# =============
#: Storage for ratelimiter.
RATELIMIT_STORAGE_URL = 'redis://localhost:6379/3'

# I18N
# ====
#: Default language
BABEL_DEFAULT_LANGUAGE = 'en'
#: Default time zone
BABEL_DEFAULT_TIMEZONE = 'Europe/Zurich'
#: Other supported languages (do not include the default language in list).
I18N_LANGUAGES = [
    # ('fr', _('French'))
]

# Base templates
# ==============
#: Global base template.
BASE_TEMPLATE = 'invenio_theme/page.html'
#: Cover page base template (used for e.g. login/sign-up).
COVER_TEMPLATE = 'invenio_theme/page_cover.html'
#: Footer base template.
FOOTER_TEMPLATE = 'invenio_theme/footer.html'
#: Header base template.
HEADER_TEMPLATE = 'invenio_theme/header.html'
#: Settings base template.
SETTINGS_TEMPLATE = 'invenio_theme/page_settings.html'

# Theme configuration
# ===================
#: Site name
THEME_SITENAME = _('ilsplayground')
#: Use default frontpage.
THEME_FRONTPAGE = True
#: Frontpage title.
THEME_FRONTPAGE_TITLE = _('ilsplayground')
#: Frontpage template.
THEME_FRONTPAGE_TEMPLATE = 'ilsplayground/frontpage.html'

# Email configuration
# ===================
#: Email address for support.
SUPPORT_EMAIL = "info@inveniosoftware.org"
#: Disable email sending by default.
MAIL_SUPPRESS_SEND = True

# Assets
# ======
#: Static files collection method (defaults to copying files).
COLLECT_STORAGE = 'flask_collect.storage.file'

# Accounts
# ========
#: Email address used as sender of account registration emails.
SECURITY_EMAIL_SENDER = SUPPORT_EMAIL
#: Email subject for account registration emails.
SECURITY_EMAIL_SUBJECT_REGISTER = _(
    "Welcome to ilsplayground!")
#: Redis session storage URL.
ACCOUNTS_SESSION_REDIS_URL = 'redis://localhost:6379/1'

# Celery configuration
# ====================

BROKER_URL = 'amqp://guest:guest@localhost:5672/'
#: URL of message broker for Celery (default is RabbitMQ).
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'
#: URL of backend for result storage (default is Redis).
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
#: Scheduled tasks configuration (aka cronjobs).
CELERY_BEAT_SCHEDULE = {
    'indexer': {
        'task': 'invenio_indexer.tasks.process_bulk_queue',
        'schedule': timedelta(minutes=5),
    },
    'accounts': {
        'task': 'invenio_accounts.tasks.clean_session_table',
        'schedule': timedelta(minutes=60),
    },
}

# Database
# ========
#: Database URI including user and password
SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://ilsplayground:ilsplayground@localhost/ilsplayground'

# JSONSchemas
# ===========
#: Hostname used in URLs for local JSONSchemas.
JSONSCHEMAS_HOST = 'localhost:5000'

# Flask configuration
# ===================
# See details on
# http://flask.pocoo.org/docs/0.12/config/#builtin-configuration-values

#: Secret key - each installation (dev, production, ...) needs a separate key.
#: It should be changed before deploying.
SECRET_KEY = 'CHANGE_ME'
#: Max upload size for form data via application/mulitpart-formdata.
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100 MiB
#: Sets cookie with the secure flag by default
SESSION_COOKIE_SECURE = True
#: Since HAProxy and Nginx route all requests no matter the host header
#: provided, the allowed hosts variable is set to localhost. In production it
#: should be set to the correct host and it is strongly recommended to only
#: route correct hosts to the application.
APP_ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# OAI-PMH
# =======
OAISERVER_ID_PREFIX = 'oai:ilsplayground.com:'

# Debug
# =====
# Flask-DebugToolbar is by default enabled when the application is running in
# debug mode. More configuration options are available at
# https://flask-debugtoolbar.readthedocs.io/en/latest/#configuration

#: Switches off incept of redirects by Flask-DebugToolbar.
DEBUG_TB_INTERCEPT_REDIRECTS = False


# PID
# ===
_BOOK_PID_TYPE = 'bookid'
_ITEM_PID_TYPE = 'itemid'
_LOCATION_PID_TYPE = 'locid'

# RECORDS REST
# ============
RECORDS_REST_ENDPOINTS = dict(
    bookid=dict(
        pid_type=_BOOK_PID_TYPE,
        pid_minter='book_pid_minter',
        pid_fetcher='book_pid_fetcher',
        search_class=BookRecordSearch,
        record_class=BookRecord,
        record_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_response'),
        },
        search_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_search'),
        },
        list_route='/books/',
        item_route='/books/<pid(bookid):pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        error_handlers=dict(),
    ),
    itemid=dict(
        pid_type=_ITEM_PID_TYPE,
        pid_minter='item_pid_minter',
        pid_fetcher='item_pid_fetcher',
        search_class=ItemRecordSearch,
        record_class=ItemRecord,
        record_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_response'),
        },
        search_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_search'),
        },
        list_route='/items/',
        item_route='/items/<pid(itemid):pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        error_handlers=dict(),
    ),
    locid=dict(
        pid_type=_LOCATION_PID_TYPE,
        pid_minter='location_pid_minter',
        pid_fetcher='location_pid_fetcher',
        search_class=LocationRecordSearch,
        record_class=LocationRecord,
        record_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_response'),
        },
        search_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_search'),
        },
        list_route='/locations/',
        item_route='/locations/<pid(locid):pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        error_handlers=dict(),
    ),
)

# RECORDS UI
# ==========
RECORDS_UI_ENDPOINTS = {
    "bookid": {
        "pid_type": _BOOK_PID_TYPE,
        "route": "/books/<pid_value>",
        "template": "invenio_records_ui/detail.html",
    },
    "bookid_export": {
        "pid_type": _BOOK_PID_TYPE,
        "route": "/books/<pid_value>/export/<format>",
        "view_imp": "invenio_records_ui.views.export",
        "template": "invenio_records_ui/export.html",
    },
    "itemid": {
        "pid_type": _ITEM_PID_TYPE,
        "route": "/items/<pid_value>",
        "template": "invenio_records_ui/detail.html",
    },
    "itemid_export": {
        "pid_type": _ITEM_PID_TYPE,
        "route": "/items/<pid_value>/export/<format>",
        "view_imp": "invenio_records_ui.views.export",
        "template": "invenio_records_ui/export.html",
    },
    "locid": {
        "pid_type": _LOCATION_PID_TYPE,
        "route": "/locations/<pid_value>",
        "template": "invenio_records_ui/detail.html",
    },
    "locid_export": {
        "pid_type": _LOCATION_PID_TYPE,
        "route": "/locations/<pid_value>/export/<format>",
        "view_imp": "invenio_records_ui.views.export",
        "template": "invenio_records_ui/export.html",
    }
}

# SEARCH UI
# =========
SEARCH_UI_SEARCH_API = '/api/books/'

SEARCH_UI_SEARCH_INDEX = 'books'


# CIRCULATION
# ===========
CIRCULATION_ITEMS_RETRIEVER_FROM_DOCUMENT = circulation_items_retriver
CIRCULATION_BOOK_RETRIEVER_FROM_ITEM = circulation_document_retriver
CIRCULATION_PATRON_EXISTS = circulation_patron_exists
CIRCULATION_ITEM_EXISTS = circulation_item_exists
CIRCULATION_ITEM_LOCATION_RETRIEVER = circulation_item_location_retriever
CIRCULATION_POLICIES['checkout']['item_available'] = circulation_is_item_available
