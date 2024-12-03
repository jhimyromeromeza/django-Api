from rest_framework import serializers
from .models import Tasks

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'done', 'created_at')
        read_only_fields = ('created_at', )