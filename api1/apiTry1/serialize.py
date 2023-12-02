from rest_framework import serializers
from .models import GangInfo

class GangInfoSerializer(serializers.ModelSerializer):
   class Meta:
      model =  GangInfo
      fields = '__all__'