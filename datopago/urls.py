from rest_framework import routers
from .views import UserViewSet,PaymentUserViewSet,ServiceViewSet,ExpiredPaymentsViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'service', ServiceViewSet, basename='service')
router.register(r'payment', PaymentUserViewSet, basename='payment')
router.register(r'expired', ExpiredPaymentsViewSet, basename='expired')

urlpatterns = router.urls