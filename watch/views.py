from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from watch.models import  Watch, Category
from watch.serializers import WatchSerializers
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly




# class WatchViewSet(viewsets.ModelViewSet):
#     queryset = Watch.objects.all()
#     serializer_class = WatchSerializers
#
#     def get_queryset(self):
#         return Watch.objects.all()[:3]
#
#     @action(methods=['GET'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'Категории':[cats.category]})




"""-------------------------------------------"""
class WatchAPIList(generics.ListCreateAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )



class WatchAPIUpdate(generics.UpdateAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializers


class WatchAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializers
"""--------------------------------------------"""
# class WatchAPIView(APIView):
#     def get(self, request):
#         w = Watch.objects.all()
#         return Response({'Посты': WatchSerializers(w,many=True).data})
#
#     def post(self, request):
#         serializer = WatchSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'Новый пост': serializer.data})
#
#
#     def put(self, request, *args, **kwargs):
#         pk  = kwargs.get('pk')
#         if not pk:
#             return Response({"Пост": 'Метод PUT не работает'})
#         try:
#             instance = Watch.objects.get(pk=pk)
#         except:
#             return Response({'Объект': 'Объект PUT не сработал'})
#         serializer = WatchSerializers(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#             # serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post':serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         instance = Watch.objects.get(pk=pk)
#         instance.delete()
#         return Response({'post': 'Delete' + str(instance)})








