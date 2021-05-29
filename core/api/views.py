from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Q

from datetime import datetime, timedelta, date as dt
# from .filters import datefilter, get_date_range as delta

from rest_framework import generics, authentication, permissions


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django_filters.rest_framework import DjangoFilterBackend

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import authentication, permissions, parsers, viewsets, mixins, status, views

# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

from core.models import (
    User, Employee, Department, AssetType, Asset, Office, AssetHistory
    )
from .serializers import (
    UserListSerializer, UserSerializer, AuthTokenSerializer, ChangePasswordSerializer,
    UserPictureSerializer,DepartmentSerializer,AssetTypeSerializer,AssetSerializer,
    OfficeSerializer,AssetHistorySerializer,
    # AttachmentSerializer,
    )
# from .pagination import PatientPagination, AppointmentPagination

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    # Manage authenticated user
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        # Retrieve and return authenticated user
        return self.request.user

class ChangePasswordView(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (permissions.IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    # Manage ingredientss in the database
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.all()
        # PERFORM FILTER BY SEARCH INPUT
        conditions = Q()
        keywords = self.request.query_params.get('input', None)
        # print(keywords)
        if keywords:
            
            keywords_list = keywords.split(' ') 
            # print(keywords_list)
            for word in keywords_list:
                conditions |= Q(name__icontains=word) | Q(email__icontains=word)
    
            if conditions:
                # print(type(conditions))
                queryset = User.objects.filter(conditions)

        return queryset

class UserImageUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserPictureSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'

 
    
    def get_object(self):
        kwarg_id = self.kwargs.get("id")
        obj = User.objects.get(id=kwarg_id)
        return obj

class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class OfficetViewset(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

class AssetTypeViewset(viewsets.ModelViewSet):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeSerializer

from rest_framework import filters
from django.db.models import Q



def filter_conditions(queryset, params=None):
    conditions = Q()
    keywords = params.get('input', None)
    # print(keywords)
    if keywords:
        
        keywords_list = keywords.split(' ') 
        # print(keywords_list)
        for word in keywords_list:
            conditions |= Q(name__icontains=word) | Q(department__name__icontains=word) | Q(office__name__icontains=word) | Q(employee__name__icontains=word)

        if conditions:
            # print(type(conditions))
            queryset = Asset.objects.filter(conditions)

        return queryset
    return queryset


class AssetViewset(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields  = ['$name', '$department', '$office','$employee']
    ordering_fields = ['name', 'department','employee','created']
    # filterset_fields = '__all__'

    def get_queryset(self):

        queryset = Asset.objects.all()
        # print(self.request.query_params)
        return filter_conditions(queryset,self.request.query_params)
        
        # conditions = Q()
        # keywords = self.request.query_params.get('name', None)
        # # print(keywords)
        # if keywords:
            
        #     keywords_list = keywords.split(' ') 
        #     # print(keywords_list)
        #     for word in keywords_list:
        #         conditions |= Q(name__icontains=word) | Q(department__name__icontains=word)
    
        #     if conditions:
        #         # print(type(conditions))
        #         queryset = Asset.objects.filter(conditions)

        # return queryset

class AssetHistoryViewset(viewsets.ModelViewSet):
    queryset = AssetHistory.objects.all()
    serializer_class = AssetHistorySerializer
