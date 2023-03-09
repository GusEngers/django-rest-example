from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Books
# Create your views here.
def server_testing(request):
    data = {"status": "Servidor funcionando!!"}
    return JsonResponse(data)
    
class BooksList(APIView):
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk is None:
            books = Books.objects.all()
            serializer = BookSerializer(books, many=True)
            if books:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        else:
            book = Books.objects.filter(pk=pk).first()
            serializer = BookSerializer(book)
            if book:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response("No se ha encontrado", status=status.HTTP_404_NOT_FOUND)