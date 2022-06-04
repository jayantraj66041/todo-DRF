from rest_framework.serializers import ModelSerializer
from api.models import TodoModel
from django.contrib.auth.models import User
from rest_framework import serializers

# todo serializer
class TodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id', 'work']

        # extra_kwargs = {
        #     'user': {"read_only": True}
        # }

    # def save(self):
    #     todo = TodoModel()
    #     todo.work = self.validated_data['work']
    #     todo.user = self.context['request'].user
    #     todo.save()

    #     return todo

# signup new user serializer
class SignUpSerializer(ModelSerializer):
    password2 = serializers.CharField(write_only=True)      # extra new field for password validation
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    # check validation
    def validate(self, data):
        if data.get("password") != data.get("password2"):
            raise serializers.ValidationError("Both password must be same.")
        
        return data
    
    # save and create new user
    def save(self):
        user = User()
        user.first_name = self.validated_data['first_name']
        user.last_name = self.validated_data['last_name']
        user.username = self.validated_data['username']
        user.email = self.validated_data['email']
        user.set_password(self.validated_data['password'])
        user.save()

        return user