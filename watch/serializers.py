from rest_framework import serializers

from watch.models import Watch


class WatchSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=500)
    brand = serializers.CharField(max_length=500)
    made_city = serializers.CharField(max_length=150)
    differences = serializers.CharField(max_length=500)
    description = serializers.CharField()
    price = serializers.IntegerField(default=0)
    cat_id_id = serializers.IntegerField()


    def create(self, validated_data):
        return Watch.objects.create(**validated_data)




