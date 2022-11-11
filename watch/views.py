from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from watch.models import  Watch
from watch.serializers import WatchSerializers


class WatchAPIView(APIView):
    def get(self, request):
        w = Watch.objects.all()
        return Response({'Посты': WatchSerializers(w,many=True).data})

    def post(self, request):
        serializer = WatchSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Новый пост': serializer.data})




