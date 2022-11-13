from django.contrib import admin
from django.urls import path, include
from watch.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'watch', WatchViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/allwatch/', WatchViewSet.as_view({'get':'list'})),
    # path('api/v1/allwatch/<int:pk>/', WatchViewSet.as_view({'put':'update'})),
    # path('api/v1/watchdetail/<int:pk>/', WatchAPIDetailView.as_view()),
]
