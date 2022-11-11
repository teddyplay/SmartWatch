from django.contrib import admin
from django.urls import path
from watch.views import WatchAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/allwatch/', WatchAPIView.as_view())
]


