from rest_framework import serializers

from watch.models import Watch


class WatchSerializers(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Watch
        fields = '__all__'


    # name = serializers.CharField(max_length=500)
    # brand = serializers.CharField(max_length=500)
    # made_city = serializers.CharField(max_length=150)
    # differences = serializers.CharField(max_length=500)
    # description = serializers.CharField()
    # price = serializers.IntegerField(default=0)
    # cat_id_id = serializers.IntegerField()
"""--------------------------------------------------------"""
    # """POST запрос"""
    # def create(self, validated_data):
    #     return Watch.objects.create(**validated_data)
    #
    # """PUT Запрос """
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.brand = validated_data.get('brand', instance.brand)
    #     instance.made_city = validated_data.get('made_city', instance.made_city)
    #     instance.differences = validated_data.get('differences', instance.differences)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.cat_id_id = validated_data.get('cat_id_id', instance.cat_id_id)
    #     instance.save()
    #     return instance








