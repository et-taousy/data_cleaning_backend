from django.contrib.auth.models import User, Group
from rest_framework import serializers
from data_cleaning.root_app.models import Address
from .models import File

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'password')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('way', 'company', 'Street_number', 'zip', 'city', 'country','byScrapy')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"