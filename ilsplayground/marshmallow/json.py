# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# My datamodel is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import DateString, SanitizedUnicode
from marshmallow import fields, missing, validate


def get_id(obj, context):
    """Get record id."""
    pid = context.get('pid')
    return pid.pid_value if pid else missing


class MetadataSchemaV1(StrictKeysMixin):
    """Schema for the record metadata."""

    def get_id(self, obj):
        """Get record id."""
        pid = self.context.get('pid')
        return pid.pid_value if pid else missing

    id = fields.Function(
        serialize=get_id,
        deserialize=get_id)
    title = SanitizedUnicode()
    authors = SanitizedUnicode()
    description = SanitizedUnicode()
    items = SanitizedUnicode()


class BookSchemaV1(StrictKeysMixin):
    """Book schema."""

    metadata = fields.Nested(MetadataSchemaV1)
    created = fields.Str(dump_only=True)
    revision = fields.Integer(dump_only=True)
    updated = fields.Str(dump_only=True)
    links = fields.Dict(dump_only=True)
    id = fields.Function(
        serialize=get_id,
        deserialize=get_id)
