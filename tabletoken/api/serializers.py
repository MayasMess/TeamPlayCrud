from rest_framework import serializers
from tabletoken.models import TableToken


class TableTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableToken
        fields = '__all__'
