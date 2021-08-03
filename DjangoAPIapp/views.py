from rest_framework import generics
from django.contrib.auth.models import User
from .models import Category, Comment, Product, Cart
from .serializers import (
    CommentsSerializer,
    RegistrationSerializer,
    CategorySerializer,
    ProductSerializer,
    UserSerializer,
    CartSerializer,
)
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid


class RegistrationAPIView(generics.GenericAPIView):
    """Register."""

    serializer_class = RegistrationSerializer

    def post(self, request):
        """post."""
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "RequestId": str(uuid.uuid4()),
                    "Message": "User created successfully",
                    "User": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class ListCategory(generics.ListCreateAPIView):
    """ListCategory."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    """DetailCategory."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListProduct(generics.ListCreateAPIView):
    """ListProduct."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListComment(generics.ListCreateAPIView):
    """ListComment."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer


class DetailComment(generics.RetrieveUpdateDestroyAPIView):
    """ListComment."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    """DetailProduct."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListUser(generics.ListCreateAPIView):
    """ListUser."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    """DetailUser."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListCart(generics.ListCreateAPIView):
    """ListCart."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    """DetailCart."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
