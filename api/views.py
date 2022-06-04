from rest_framework.views import APIView
from api.models import TodoModel
from api.serializers import SignUpSerializer, TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class SignUp(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Login(APIView):
#     def post(self, request):
#         pass

class Todo(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todo = TodoModel.objects.filter(user=request.user)
        serializer = TodoSerializer(todo, many=True)
        return Response({
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
            'todo': serializer.data
        })

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                'message': "Todo saved successfully."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        todo = TodoModel.objects.get(id=id)
        if todo.user.id == request.user.id:
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Invalid Id"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        todo = TodoModel.objects.get(id=id)
        if todo.user.id == request.user.id:
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Invalid Id"}, status=status.HTTP_400_BAD_REQUEST)