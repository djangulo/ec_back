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


class PressDateSerializer(serializers.Serializer):
    dates = serializers.SerializerMethodField()
    
    class Meta:
        model = Press

    def get_dates(self, obj):
        return {
            'year': obj.year,
            'month': obj.month,
        }


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
            'url',
            'press_kit',
            'display_order',
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


class ShortCoverSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('image',)
        model = WorkCover


class WorksByCategorySerializer(serializers.ModelSerializer):
    category= serializers.CharField(source='category.slug', read_only=True)
    status = serializers.CharField(source='status.slug', read_only=True)
    program = serializers.CharField(source='program.slug', read_only=True)
    cover = ShortCoverSerializer(read_only=True)
    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'cover',
            'team',
            'status',
            'program',
            'published_date',
            'display_order',
        )
        model = Work


class WorkSerializer(serializers.ModelSerializer):
    pictures = WorkPictureSerializer(many=True, read_only=True)
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
            'display_order',
        )
        model = Work
        
        


class PublicationSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(source='category.id', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    medium_id = serializers.CharField(source='medium.id', read_only=True)
    medium_slug = serializers.CharField(source='medium.slug', read_only=True)
    medium_name = serializers.CharField(source='medium.name', read_only=True)
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
            'medium_name',
            'url',
            'image',
            'display_order',
        )
        model = Publication
