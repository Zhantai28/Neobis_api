from rest_framework import serializers
from .models import Category, Product, Cart, Comment, Replies
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """RegistrationSerializer."""

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        """Meta."""

        model = User
        fields = ("id", "first_name", "last_name",
                  "email", "username", "password")

    def validate(self, args):
        """validate."""
        email = args.get("email", None)
        username = args.get("username", None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": ("email already exists")})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": ("username already exists")})

        return super().validate(args)

    def create(self, validated_data):
        """create."""
        return User.objects.create_user(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    """CategorySerializer."""

    class Meta:
        """Meta."""

        fields = ("id", "title")
        model = Category


class RepliesSerializer(serializers.ModelSerializer):
    """RepliesSerializer."""

    class Meta:
        """Meta."""

        model = Replies
        fields = ("author", "content")


class CommentsSerializer(serializers.ModelSerializer):
    """CommentsSerializer."""

    class Meta:
        """Meta."""

        fields = ("id", "author", "rate", "content", "product", "created_at")
        model = Comment


class CommentSerializer(serializers.ModelSerializer):
    """CommentSerializer."""

    replies = serializers.SerializerMethodField()

    class Meta:
        """Meta."""

        model = Comment
        fields = ("id", "author", "rate", "content", "replies")

    def get_replies(self, obj):
        """get_replies."""
        selected_replies = Replies.objects.filter(comment=obj).distinct()
        return RepliesSerializer(selected_replies, many=True).data


class ProductSerializer(serializers.ModelSerializer):
    """ProductSerializer."""

    created_by = serializers.ReadOnlyField(
        source="created_by.username", read_only=False
    )

    comments = serializers.SerializerMethodField()

    class Meta:
        """Meta."""

        fields = (
            "id",
            "title",
            "desc",
            "imageUrl",
            "price",
            "supplier",
            "price",
            "category",
            "created_by",
            "date_created",
            "comments",
        )
        model = Product

    def get_comments(self, obj):
        """get_comments."""
        selected_comments = Comment.objects.filter(product=obj).distinct()
        return CommentSerializer(selected_comments, many=True).data


class UserSerializer(serializers.ModelSerializer):
    """UserSerializer."""

    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all()
    )

    class Meta:
        """Meta."""

        model = User
        fields = (
            "id",
            "username",
            "email",
            "products",
        )


class CartUserSerializer(serializers.ModelSerializer):
    """CartUserSerializer."""

    class Meta:
        """Meta."""

        model = User
        fields = ("username", "email")


class CartSerializer(serializers.ModelSerializer):
    """CartSerializer."""

    cart_id = CartUserSerializer(read_only=True, many=False)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        """Meta."""

        model = Cart
        fields = ("cart_id", "created_at", "products", "quantity")
