# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
# Copyright (C) 2018 RERO.
#
# Invenio-Circulation is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Circulation minters."""

from ..config import _BOOK_PID_TYPE, _ITEM_PID_TYPE, _LOCATION_PID_TYPE
from .providers import BookIdProvider, ItemIdProvider, LocationIdProvider


def book_pid_minter(record_uuid, data):
    """Mint book identifiers."""
    assert _BOOK_PID_TYPE not in data
    provider = BookIdProvider.create(
        object_type='rec',
        object_uuid=record_uuid,
    )
    data[_BOOK_PID_TYPE] = provider.pid.pid_value
    return provider.pid


def item_pid_minter(record_uuid, data):
    """Mint item identifiers."""
    assert _ITEM_PID_TYPE not in data
    provider = ItemIdProvider.create(
        object_type='rec',
        object_uuid=record_uuid,
    )
    data[_ITEM_PID_TYPE] = provider.pid.pid_value
    return provider.pid


def location_pid_minter(record_uuid, data):
    """Mint location identifiers."""
    assert _LOCATION_PID_TYPE not in data
    provider = LocationIdProvider.create(
        object_type='rec',
        object_uuid=record_uuid,
    )
    data[_LOCATION_PID_TYPE] = provider.pid.pid_value
    return provider.pid
