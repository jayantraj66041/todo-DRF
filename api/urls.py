from django.urls import path
from api.views import SignUp, Todo
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path("signup/", SignUp.as_view()),
    path('todo/', Todo.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path("verify/", TokenVerifyView.as_view()),
]
