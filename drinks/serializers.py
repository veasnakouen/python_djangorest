# this going to describe the process from python object to json
from rest_framework import serializers #type:ignore
from .models import Drink,Post


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id','name','description']


# serializer using Model serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        # fields = '__all__'
        fields = ['id','title','author','email']


# using Serializer
# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=150)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(default='')

#     def create(self,validate_data): 
#         return Post.objects.create(validate_data)
    
#     def update(self,instance,validated_data):
#         instance.title = validated_data.get('title',validated_data.title)
#         instance.author = validated_data.get('author',validated_data.author)
#         instance.email = validated_data.get('email',validated_data.email)