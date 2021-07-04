from .models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(input_formats=['%Y-%m-%d'], format='%Y-%m-%d', read_only=True)
    updated_at = serializers.DateTimeField(input_formats=['%Y-%m-%d'], format='%Y-%m-%d', read_only=True)
    photo = serializers.ImageField(source='created_by.photo', read_only=True)
    user = serializers.CharField(source='created_by.username', read_only=True)

    def validate(self, attrs):
        if len(attrs['short_description']) < 3:
            raise serializers.ValidationError("Cannot be less than 3 chars")
        return attrs

    class Meta:
        model = Todo
        fields = ['created_by', 'short_description', 'long_description', 'allocated_time', 'created_at',
                  'user', 'is_complete', 'updated_at', 'photo']
        # fields = '__all__'
        validators = []


class TodoCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

