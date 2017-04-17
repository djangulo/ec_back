import datetime
from rest_framework import serializers

from . import models

class CategorySerializer(serializers.ModelSerializer):
    # publications = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True
    # )
    # press_releases = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True,
    # )
    class Meta:
        fields = (
            'id',
            'name',
            'slug',
            'description'
        )
        model = models.Category



class PressReleaseSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(source='category.id', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category_id',
            'category_slug',
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

# class ChoiceFieldField(serializers.RelatedField):
#     def to_representation(self, instance, obj=None):
#         instan



class WorkSerializer(serializers.ModelSerializer):
    pictures = WorkPictureSerializer(many=True, read_only=True)
    # category = CategorySerializer(many=False, read_only=True)
    category_id = serializers.CharField(source='category.id', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category_id',
            'category_slug',
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
    category_id = serializers.CharField(source='category.id', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    medium = serializers.CharField(source='get_medium_display')
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category_id',
            'category_slug',
            'medium',
            'image'
        )
        model = models.Publication


class CategorySerializer(serializers.ModelSerializer):
    # works = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True
    # )
    # publications = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True
    # )
    # press_releases = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True,
    # )
    class Meta:
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'works',
            'press_releases',
            'publications'
        )
        model = models.Category
