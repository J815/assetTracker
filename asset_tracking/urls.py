# urls.py

from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, DeviceLogViewSet,DeviceTypeViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'devicetypes', DeviceTypeViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'devicelogs', DeviceLogViewSet)

urlpatterns = router.urls
