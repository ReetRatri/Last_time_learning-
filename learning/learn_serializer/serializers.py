from rest_framework import serializers
from .models import Book , Author

class Book_serializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = ('__all__')


 


#  when er have to validate only ...... tb hm basic serializer use krte hai 

class Author_serializer(serializers.Serializer):
    author =  serializers.CharField(max_length=200)
    number_of_books = serializers.IntegerField()

    print(author)
    print(number_of_books)

    def caluclete(self ,number_of_books ):
        number_of_books = number_of_books * 10
        return number_of_books
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['number_of_books'] = self.caluclete(instance.number_of_books)
        return data
    
    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if 'author' in data:    
            data['author']  = data['author'].upper()
        return data
    
    def get_fields(self):
        feilds = super().get_fields()
        print(feilds)
        return feilds
    



    def create(self, validated_data):
        author_instance = Author.objects.create(**validated_data)
        print('-----------------------')
        print('-----------------------')
        print('-----------------------')
        print(validated_data , 'created--=-====-=')
        return author_instance 
        # return super().create(validated_data)