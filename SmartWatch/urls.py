from django.contrib import admin
from django.urls import path
from watch.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/allwatch/', WatchAPIList.as_view()),
    path('api/v1/allwatch/<int:pk>/', WatchAPIUpdate.as_view()),
    path('api/v1/watchdetail/<int:pk>/', WatchAPIDetailView.as_view()),
]
