from rest_framework import serializers

from .models import HomeImage


class HomeImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'image',
            'caption',
            'order'
        )
        model = HomeImage