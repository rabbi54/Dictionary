from django.db import models


class CommaSeparatedStringsField(models.CharField):

    def from_db_value(self, value, *args):
        if not value:
            return []

        return value.split(',')

    def to_python(self, value):
        if isinstance(value, list):
            return value

        return self.from_db_value(value)

    def get_prep_value(self, value):
        return ','.join(value)

    def value_to_string(self, obj):
        return self.get_prep_value(self.value_from_object(obj))


class QuoteSeparatedStringsField(models.CharField):

    def from_db_value(self, value, *args):
        if not value:
            return []

        return value.split('"')

    def to_python(self, value):
        if isinstance(value, list):
            return value

        return self.from_db_value(value)

    def get_prep_value(self, value):
        return ','.join(value)

    def value_to_string(self, obj):
        return '"' + self.get_prep_value(self.value_from_object(obj)) + '"'
