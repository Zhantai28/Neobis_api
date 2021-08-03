from rest_framework.test import APITestCase
from DjangoAPIapp.models import Category, Product, Comment, Replies
from django.contrib.auth.models import User


class TestModel(APITestCase):
    """TestModel."""

    def test_category(self):
        """test_category."""
        category = Category.objects.create(title="asd")
        self.assertEqual(category.title, "asd")
        self.assertIsInstance(category, Category)

    def test_product(self):
        """test_product."""
        category = Category.objects.create(title="asd")
        user = User.objects.create(
            username="admin", password="123", email="admin@gmail.com"
        )
        product = Product.objects.create(
            title="asd",
            desc="qew",
            imageUrl="hehal",
            price=12,
            discount=0,
            supplier="as",
            category=category,
            created_by=user,
        )
        self.assertIsInstance(product, Product)
        self.assertEqual(product.desc, "qew")
        self.assertEqual(user.email, "admin@gmail.com")

    def test_comment(self):
        """test_comment."""
        category = Category.objects.create(title="asd")
        user = User.objects.create(
            username="admin", password="123", email="admin@gmail.com"
        )
        product = Product.objects.create(
            title="asd",
            desc="qew",
            imageUrl="hehal",
            price=12,
            discount=0,
            supplier="as",
            category=category,
            created_by=user,
        )
        comment = Comment.objects.create(
            author=user, rate=4, content="hello hello", product=product
        )
        self.assertIsInstance(comment, Comment)
        self.assertEqual(comment.rate, 4)

    def test_replies(self):
        """test_replies."""
        category = Category.objects.create(title="asd")
        user = User.objects.create(
            username="admin", password="123", email="admin@gmail.com"
        )
        product = Product.objects.create(
            title="asd",
            desc="qew",
            imageUrl="hehal",
            price=12,
            discount=0,
            supplier="as",
            category=category,
            created_by=user,
        )
        comment = Comment.objects.create(
            author=user, rate=4, content="hello hello", product=product
        )
        replies = Replies.objects.create(
            author=user, comment=comment, content="asfgdqew"
        )
        self.assertIsInstance(replies, Replies)
        self.assertEqual(replies.content, "asfgdqew")
