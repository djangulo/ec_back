from rest_framework import serializers

from . import models

class PressReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'category',
            'date_released'
        )
        model = models.PressRelease


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'category',
            'team',
            'status',
            'program'
        )
        model = models.Work


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'category',
            'type'
        )
        model = models.Publication