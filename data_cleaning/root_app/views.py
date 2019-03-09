from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from data_cleaning.root_app.models import Address
from data_cleaning.root_app.serializers import UserSerializer, GroupSerializer, AddressSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AddressViewSet(viewsets.ModelViewSet):

    #API endpoint that allows groups to be viewed or edited.

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
