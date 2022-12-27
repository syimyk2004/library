from rest_framework.views import APIView
from book.models import Book
from book.serializers import BookSerializers
from rest_framework.response import Response
from rest_framework import status

from  rest_framework.exceptions import ValueDationError

class BookAPIView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializers = BookSerializers(books, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = BookSerializers(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BookDetailUpdateDeleteAPIView(APIView):
    def get(self, requst, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer = BookSerializers(books)
            return Response(serializer.data)
        except Book.DoesNotExist as error:
            raise ValueDationError(
                {'error': err}
            )
    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializers(books, data=request.data)
        if serializer.is_valid():
            serializer.save()


class BookUpdateSerializer(serializers.ModelSerializer):
    model = Book 
    fieds = '__all__'
    extra_kwargs = { "author": {"required": False},
                     "year": {'required': False},
                     "desc": {"required": False},
                     "title": {'required': False}
    
    
                }

    def update(self, instance, validated_data):
        instance.year = validated_data.get("year", instance.year)
        instance.title = validated_data.get("title", instance.title)
        instance.desc = validated_data.get("desc", instance.desc)
        instance.author = validated_data.get("author", instance.author)
        instance.save()
        return instance
