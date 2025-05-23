from rest_framework import routers
from .views import DepartmentViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = router.urls
