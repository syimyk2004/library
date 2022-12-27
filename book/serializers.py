from rest_framework import serializers
from.models import Book, Picture

# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField()
#     desc = serializers.CharField()
#     author = serializers.CharField()
#     year = serializers.IntegerField()
class PrictureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'


class BookSerializers(serializers.ModelSerializer):
    genre = serializers.CharField(source='genre.title')
    class Meta:
        model = Book 
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.genre:
            representation['genre']=instance.genre.title
        if instance.books_pictures.exists():
            representation['pictures'] = PrictureSerializers(instance.books_pictures.all(), many=True).data
        
        return representation