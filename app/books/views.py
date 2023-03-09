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
    
class PostAndList(APIView):

    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": f"Libro {serializer.data['title']} creado con éxito"}, status = status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        if books:
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": "La lista de libros está vacia"}, status=status.HTTP_404_NOT_FOUND)

class OneDetail(APIView):

    def get_one(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            return "El libro solicitado no existe"
    
    def get(self, request, pk):
        book = self.get_one(pk)
        if type(book) == str:
            return Response({"error": book}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        book = self.get_one(pk)
        if type(book) == str:
            return Response({"error": book}, status=status.HTTP_404_NOT_FOUND)

        rd = request.data
        updates = {
            "title": rd["title"] if "title" in rd else getattr(book, "title"),
            "genre": rd["genre"] if "genre" in rd else getattr(book, "genre"),
            "year": rd["year"] if "year" in rd else getattr(book, "year"),
            "author": rd["author"] if "author" in rd else getattr(book, "author")
        }
        serializer = BookSerializer(book, data=updates)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": f"Libro {serializer.data['title']} actualizado", "upd": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors})
        