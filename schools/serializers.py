from rest_framework import serializers
from .models import NSWSchool

class NSWSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = NSWSchool
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.createdate is None:
            representation['createdate'] = None  # Handle null date gracefully
        if instance.modifieddate is None:
            representation['modifieddate'] = None  # Handle null date gracefully
        return representation
