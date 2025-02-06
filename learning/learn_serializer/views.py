from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import Book_serializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([AllowAny])  # Allow all users to access
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = Book_serializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = Book_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:  # Corrected condition
        book_id = request.data.get('id')
        if not book_id:
            return Response({'error': 'id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = Book_serializer(book, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book_id = request.data.get('id')  # Get book ID from request data
        if not book_id:
            return Response({'error': 'id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_404_NOT_FOUND)

        book.delete()  # Delete the book
        return Response({'message': 'book deleted successfully'}, status=status.HTTP_200_OK)
