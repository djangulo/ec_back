import datetime
from rest_framework import serializers

from . import models


class PressReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'category',
            'date_released',
            'url'
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

class WorkPictureSerializer(serializers.ModelSerializer):
    work = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        fields = (
            'id',
            'title',
            'image',
            'caption',
            'work',
            'is_cover'
        )
        model = models.WorkPicture


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'category',
            'type',
            'image'
        )
        model = models.Publication


class CategorySerializer(serializers.ModelSerializer):
    works = WorkSerializer(
        many=True,
        read_only=True,
        # view_name='api-v1:works_by_category'
    )
    publications = PublicationSerializer(
        many=True,
        read_only=True,
        # view_name='api-v1:publications_by_category'
    )
    press_releases = PressReleaseSerializer(
        many=True,
        read_only=True,
        # view_name='api-v1:press_releases_by_category'
    )
    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'works',
            'press_releases',
            'publications'
        )
        model = models.Category
