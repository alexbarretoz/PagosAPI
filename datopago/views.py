#from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Userx,PaymentUser,Service,ExpiredPayments
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializer import UserSerializer,PaymentUserSerializer, ServiceSerializer,ExpiredPaymentsSerializer
from .pagination import SimplePagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserViewSet(ModelViewSet):
    #2 atributo recibe modelviewset  queryset, serializer_class

    queryset = Userx.objects.all()
    serializer_class = UserSerializer
    pagination_class = SimplePagination
    throttle_scope = '2mil'
    permission_classes = [IsAuthenticated]    
    

class PaymentUserViewSet(ModelViewSet):
    #2 atributo recibe modelviewset  queryset, serializer_class

    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUserSerializer
    pagination_class = SimplePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['expiration_date','payment_date'] #buscar
    throttle_scope = 'mil'
    permission_classes = [IsAuthenticated]


class ServiceViewSet(ModelViewSet):
#2 atributo recibe modelviewset  queryset, serializer_class

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = SimplePagination
    throttle_scope = '2mil'
    permission_classes = [IsAuthenticated]  


class ExpiredPaymentsViewSet(ModelViewSet):
#2 atributo recibe modelviewset  queryset, serializer_class

    queryset = ExpiredPayments.objects.all()
    serializer_class = ExpiredPaymentsSerializer
    pagination_class = SimplePagination
    throttle_scope = '2mil'
    permission_classes = [IsAuthenticated]

