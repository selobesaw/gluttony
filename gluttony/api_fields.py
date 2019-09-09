import base64
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, image = data.split(';base64,')
            extension = format.split('/')[-1]
            # UUID хорош тем, что зависит от времени его создания, поэтому имена не должны пересекаться
            # как минимум до нашей смерти
            data = ContentFile(base64.b64decode(image), name=str(uuid.uuid4()) + '.' + extension)
        return super().to_internal_value(data)
