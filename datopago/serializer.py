from rest_framework.serializers import ModelSerializer
from .models import Userx,PaymentUser,Service,ExpiredPayments

class UserSerializer(ModelSerializer):
    #recibe el modelo (tabla)
    class Meta:
        model = Userx
        # all significa todo los campos
        fields = "__all__"


class PaymentUserSerializer(ModelSerializer):
    #recibe el modelo (tabla)
    class Meta:
        model = PaymentUser
        # all significa todo los campos
        fields = "__all__"


class ServiceSerializer(ModelSerializer):
    #recibe el modelo (tabla)
    class Meta:
        model = Service
        # all significa todo los campos
        fields = "__all__"



class ExpiredPaymentsSerializer(ModelSerializer):
    #recibe el modelo (tabla)
    class Meta:
        model = ExpiredPayments
        # all significa todo los campos
        fields = "__all__"