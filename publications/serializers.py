import datetime
from django.template.defaultfilters import slugify
from rest_framework import serializers

from . import models


class PressReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category',
            'created_date',
            'published_date',
            'url'
        )
        model = models.PressRelease


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


class WorkSerializer(serializers.ModelSerializer):
    pictures = WorkPictureSerializer(many=True, read_only=True)
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category',
            'document',
            'pictures',
            'team',
            'status',
            'program',
            'created_date',
            'published_date',
        )
        model = models.Work


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category',
            'medium',
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
