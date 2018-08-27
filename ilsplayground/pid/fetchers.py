# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
# Copyright (C) 2018 RERO.
#
# Invenio-Circulation is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Circulation fetchers."""

from invenio_pidstore.fetchers import FetchedPID

from ..config import _DOCUMENT_PID_TYPE, _ITEM_PID_TYPE


def document_pid_fetcher(record_uuid, data):
    """."""
    return FetchedPID(
        provider=None,
        pid_type=_DOCUMENT_PID_TYPE,
        pid_value=str(data[_DOCUMENT_PID_TYPE])
    )

def item_pid_fetcher(record_uuid, data):
    """."""
    return FetchedPID(
        provider=None,
        pid_type=_ITEM_PID_TYPE,
        pid_value=str(data[_ITEM_PID_TYPE])
    )
