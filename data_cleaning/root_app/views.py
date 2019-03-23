from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from data_cleaning.root_app.models import Address, File
from data_cleaning.root_app.serializers import UserSerializer, GroupSerializer, AddressSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import csv
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




from .serializers import FileSerializer


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
        #Address.objects.delete()
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            print(file_serializer.data)
            with open(file_serializer.data['file']) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    else:
                        print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                        address = Address()
                        address.company = row[0]
                        address.street = row[1]
                        address.city = row[2]
                        address.state = row[3]
                        address.zip = int(0)
                        address.byScrapy = False
                        address.country = row[5]
                        address.save()
                        line_count += 1
                print(f'Processed {line_count} lines.')

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

