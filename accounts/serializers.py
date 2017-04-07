from rest_framework import serializers

from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'photo',
            'bio',
            'is_active',
            'is_admin',
            'staff_or_intern'
        )
        model = models.User