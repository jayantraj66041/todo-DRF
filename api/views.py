from rest_framework.views import APIView
from api.models import TodoModel
from api.serializers import SignUpSerializer, TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# new user signup view
class SignUp(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# login work
# class Login(APIView):
#     def post(self, request):
#         pass

# Todo work
class Todo(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # function to get all todo list of the authorized user
    def get(self, request):
        todo = TodoModel.objects.filter(user=request.user)
        serializer = TodoSerializer(todo, many=True)
        
        return Response({
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
            'todo': serializer.data
        })

    # save new list
    def post(self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                'message': "Todo saved successfully."
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # update or change perform on the existing list 
    def put(self, request, id):
        todo = TodoModel.objects.get(id=id, user=request.user)

        if todo.user.id == request.user.id:
            serializer = TodoSerializer(todo, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({"error": "Invalid Id"}, status=status.HTTP_400_BAD_REQUEST)

    # for delete any list item of work
    def delete(self, request, id):
        todo = TodoModel.objects.get(id=id, user=request.user)

        if todo.user.id == request.user.id:
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({"error": "Invalid Id"}, status=status.HTTP_400_BAD_REQUEST)