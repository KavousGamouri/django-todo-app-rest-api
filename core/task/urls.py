from django.urls import path, include
from . import views

app_name = 'task'
urlpatterns = [
    path('api/v1/', include('task.api.v1.urls')),
]
