import datetime
from rest_framework import serializers

from .models import Press, Publication, Work, WorkCover, WorkPicture
from .support_models import Category, Medium, Program, Status


class CategorySerializer(serializers.ModelSerializer):
    publications = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='apiv1:publication-detail'
    )
    presses = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='apiv1:press-detail'
    )
    works = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='apiv1:work-detail'
    )
    class Meta:
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'presses',
            'publications',
            'works'
        )
        model = Category


class PressSerializer(serializers.ModelSerializer):
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
        model = Press


class WorkPictureSerializer(serializers.ModelSerializer):
    work = serializers.CharField(source='work.title', read_only=True)

    class Meta:
        fields = (
            'id',
            'title',
            'image',
            'caption',
            'work'
        )
        model = WorkPicture
        
class WorkCoverSerializer(serializers.ModelSerializer):
    work = serializers.CharField(source='work.title', read_only=True)

    class Meta:
        fields = (
            'id',
            'title',
            'image',
            'caption',
            'work'
        )
        model = WorkCover


class WorkSerializer(serializers.ModelSerializer):
    # pictures = WorkPictureSerializer(many=True, read_only=True)
    category_id = serializers.CharField(source='category.id', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    status = serializers.CharField(source='status.slug', read_only=True)
    program = serializers.CharField(source='program.slug', read_only=True)
    cover = WorkCoverSerializer(many=False)
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category_id',
            'category_slug',
            'document',
            'cover',
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
