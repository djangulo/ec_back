import datetime
from rest_framework import serializers

from .models import (
    Category,
    Medium,
    Press,
    Program,
    Publication,
    Status,
    Work,
    WorkPicture
)


class SupportModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'slug',
            'description',
        )


class CategorySerializer(SupportModelSerializer):
    class Meta(SupportModelSerializer.Meta):
        model = Category


class StatusSerializer(SupportModelSerializer):
    class Meta(SupportModelSerializer.Meta):
        model = Status


class MediumSerializer(SupportModelSerializer):
    class Meta(SupportModelSerializer.Meta):
        model = Medium


class ProgramSerializer(SupportModelSerializer):
    category
    class Meta(SupportModelSerializer.Meta):
        model = Medium


class PressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category',
            'category',
            'created_date',
            'published_date',
            'url'
        )
        model = Press

class WorkCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPicture
        fields = (
            'id',
            'image',
            'caption'
        )


class WorkPictureSerializer(serializers.ModelSerializer):
    work = serializers.CharField(source='work.title', read_only=True)

    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'image',
            'caption',
            'work'
        )
        model = WorkPicture
        

class WorkSerializer(serializers.ModelSerializer):
    cover = WorkCoverSerializer(many=False)
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category',
            'document',
            'cover',
            'team',
            'status',
            'program',
            'created_date',
            'published_date',
        )
        model = Work


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
        model = Publication
