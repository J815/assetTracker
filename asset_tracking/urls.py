# urls.py
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, DeviceLogViewSet,DeviceTypeViewSet,LogoutView,UserRegistrationView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'devicetypes', DeviceTypeViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'devicelogs', DeviceLogViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('login',obtain_auth_token,name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('register',UserRegistrationView.as_view(),name='register'),

]
    
