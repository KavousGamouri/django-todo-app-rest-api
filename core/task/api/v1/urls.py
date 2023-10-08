from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='tasks')
urlpatterns = router.urls
