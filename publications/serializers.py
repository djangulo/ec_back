import datetime
from rest_framework import serializers

from .models import PressRelease, Publication, Work, WorkPicture
from .support_models import Category, Medium, Program, Status


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
        model = Category


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
        model = PressRelease


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
        model = WorkPicture


class WorkSerializer(serializers.ModelSerializer):
    pictures = WorkPictureSerializer(many=True, read_only=True)
    category_id = serializers.CharField(source='category.id', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    status = serializers.CharField(source='status.slug', read_only=True)
    program = serializers.CharField(source='program.slug', read_only=True)
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
        model = Work


class PublicationSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(source='category.id', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    medium_id = serializers.CharField(source='medium.id', read_only=True)
    medium_slug = serializers.CharField(source='medium.slug', read_only=True)
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category_id',
            'category_slug',
            'medium_id',
            'medium_slug',
            'image'
        )
        model = Publication
