from django.contrib import admin
from django.urls import path, include
from watch.views import *
from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'watch', WatchViewSet)
# print(router.urls)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),
    path('api/v1/allwatch/', WatchAPIList.as_view()),
    path('api/v1/allwatch/<int:pk>/', WatchAPIUpdate.as_view()),
    path('api/v1/watchdetail/<int:pk>/', WatchAPIDetailView.as_view()),
]
