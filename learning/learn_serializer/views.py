from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Book ,Author
from .serializers import Book_serializer ,Author_serializer


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

@api_view(['POST' , 'GET' , 'DELETE'])
@permission_classes([AllowAny])
def author_list(request):
    
    if request.method == 'POST':
        serializer = Author_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "status" : False , 
                    "message" : "Invalid data" ,
                    "errors" : serializer.errors
                    
                    },
                    status=status.HTTP_400_BAD_REQUEST
                    )
        print(serializer.validated_data)
        author = serializer.save()
        
        
        return Response(
                {
                    "status" : True , 
                    "message" : " recoded" ,
                    "errors" : serializer.data
                    
                    },
                   status=status.HTTP_201_CREATED
                    )
    elif request.method == 'GET':
        print(',ethod is get')
        authors = Author.objects.all()  
        serializer = Author_serializer(authors, many=True)
        if not serializer.data:
            return Response({'error': 'no authors found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
       
    elif request.method == 'DELETE':
        author = request.data.get('author')
        try:
            author = Author.objects.get(author=author)
            
        except Author.DoesNotExist:
            return Response({'message': 'author not found'}, status=status.HTTP_404_NOT_FOUND)
        
        author.delete()
        return Response({'message': 'done'})


            

        