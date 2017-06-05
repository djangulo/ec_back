import os
from rest_framework import serializers

from django.conf import settings

from .models import HomeImage


class HomeImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'image',
            'caption',
            'display_order'
        )
        model = HomeImage

class HomeTextSerializer(serializers.Serializer):
    text = serializers.SerializerMethodField()
    
    def get_text(self, obj):
        f = open(os.path.join(settings.BASE_DIR, 'home_text.txt'), 'r+')
        t = f.read()
        f.close()
        return t
        