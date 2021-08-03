from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """Category."""

    title = models.CharField(max_length=255)

    class Meta:
        """Meta."""

        verbose_name_plural = "Categories"

    def __str__(self):
        """name."""
        return self.title


class Product(models.Model):
    """Product."""

    title = models.CharField(max_length=250)
    desc = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    imageUrl = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    supplier = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        "auth.User", related_name="products", on_delete=models.CASCADE
    )

    def __str__(self):
        """name."""
        return self.title


class Cart(models.Model):
    """Cart."""

    cart_id = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=0)

    class Meta:
        """Meta."""

        ordering = ["cart_id", "-created_at"]

    def __str__(self):
        """name."""
        return f"{self.cart_id}"


class Comment(models.Model):
    """Comment."""

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    rate = models.CharField(
        max_length=1,
        choices=(
            ("1", 1),
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
        ),
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        """name."""
        return f"{self.author} {self.rate} {self.product}"


class Replies(models.Model):
    """Replies"""

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} {self.comment}"
