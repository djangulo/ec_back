from rest_framework import serializers

from . import models

class UserSerializer(serializers.ModelSerializer):
    staff_or_intern = serializers.CharField(
        source="get_staff_or_intern_display",
    )
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
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


