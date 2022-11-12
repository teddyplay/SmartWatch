from django.contrib import admin
from django.urls import path
from watch.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/allwatch/', WatchAPIList.as_view()),
    path('api/v1/allwatch/<int:pk>/', WatchAPIView.as_view()),
    path('api/v1/allwatch/<str:pk>/', WatchAPIList.as_view()),
]
