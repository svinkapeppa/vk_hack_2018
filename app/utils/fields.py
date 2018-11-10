import io
import json
import uuid

from PIL import Image
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos.error import GEOSException
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import FileField
from django.utils import six
from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class ResizeImageField(models.ImageField):
    def __init__(self, *args, **kwargs):
        self.width = kwargs.pop('width', 1000)
        self.height = kwargs.pop('height', 1000)
        super(ResizeImageField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        file = super(FileField, self).pre_save(model_instance, add)
        if file and not file._committed:
            field = getattr(model_instance, self.attname)
            f_img = field.file
            img = Image.open(f_img)
            width = img.width
            height = img.height
            if self.height < height or self.width < width:
                img.thumbnail((self.width, self.height), Image.ANTIALIAS)
            imgByteArr = io.BytesIO()
            img.convert('RGB').save(imgByteArr, format='JPEG')
            imgByteArr = imgByteArr.getvalue()
            f_img = SimpleUploadedFile(name='name.jpg', content=imgByteArr, content_type='image/jpeg')
            setattr(model_instance, self.attname, f_img)
            file.save(uuid.uuid4().hex + '.jpg', f_img, save=False)
        return file


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
                latitude = value.get('latitude')
                longitude = value.get('longitude')
                return GEOSGeometry('POINT(%(longitude)s %(latitude)s)' % {
                    'longitude': longitude,
                    'latitude': latitude}
                                    )
            except (GEOSException, ValueError):
                self.fail('invalid')
        self.fail('invalid')

    def to_representation(self, value):
        if value is None:
            return value

        if isinstance(value, GEOSGeometry):
            value = {
                'latitude': value.y,
                'longitude': value.x
            }

        if self.str_points:
            value['longitude'] = smart_str(value.pop('longitude'))
            value['latitude'] = smart_str(value.pop('latitude'))

        return value
