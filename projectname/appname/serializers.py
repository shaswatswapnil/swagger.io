from rest_framework import serializers
from .models import GoogleSheetData

class GoogleSheetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleSheetData
        fields = '__all__'