import json

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos.error import GEOSException
from django.utils import six
from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

EMPTY_VALUES = (None, '', [], (), {})


class PointField(serializers.Field):
    type_name = 'PointField'
    type_label = 'point'

    default_error_messages = {
        'invalid': _('Enter a valid location.'),
    }

    def __init__(self, *args, **kwargs):
        self.str_points = kwargs.pop('str_points', False)
        super(PointField, self).__init__(*args, **kwargs)

    def to_internal_value(self, value):
        if value in EMPTY_VALUES and not self.required:
            return None

        if isinstance(value, six.string_types):
            try:
                value = value.replace("'", '"')
                value = json.loads(value)
            except ValueError:
                self.fail('invalid')

        if value and isinstance(value, dict):
            try:
                latitude = value.get("latitude")
                longitude = value.get("longitude")
                return GEOSGeometry('POINT(%(longitude)s %(latitude)s)' % {
                    "longitude": longitude,
                    "latitude": latitude}
                                    )
            except (GEOSException, ValueError):
                self.fail('invalid')
        self.fail('invalid')

    def to_representation(self, value):
        if value is None:
            return value

        if isinstance(value, GEOSGeometry):
            value = {
                "latitude": value.y,
                "longitude": value.x
            }

        if self.str_points:
            value['longitude'] = smart_str(value.pop('longitude'))
            value['latitude'] = smart_str(value.pop('latitude'))

        return value
