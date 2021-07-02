from .models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        if len(attrs['short_description']) < 3:
            raise serializers.ValidationError("Cannot be less than 3 chars")
        return attrs

    class Meta:
        model = Todo
        # fields = ['short_description', 'long_description', 'allocated_time', 'created_at',
        #           'created_by', 'is_complete', 'updated_at']
        fields = '__all__'
        validators = []


