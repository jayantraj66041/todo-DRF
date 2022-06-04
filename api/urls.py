from django.urls import path
from api.views import SignUp, Todo
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("signup/", SignUp.as_view()),              # signup url
    path('todo/', Todo.as_view()),                  # todo view and create
    path('todo/<int:id>/', Todo.as_view()),         # todo update or delete
    path('token/', TokenObtainPairView.as_view()),  # generate new token (login)
]
