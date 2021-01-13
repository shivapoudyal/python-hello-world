from rest_framework import serializers
from models import teams
from models import teamcrud
from models import my_custom_sql


class teamSerializers(serializers.ModelSerializer):
    class Meta:
        model = teamcrud
        fields = ('id', 'name', 'designation', 'img', 'status', 'is_deleted')
        # fields = '__all__'