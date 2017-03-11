from rest_framework import serializers

from sneakers.models import Sneaker


class SneakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sneaker
        fields = ('pk', 'label', 'info', 'created_at', 'feature')
