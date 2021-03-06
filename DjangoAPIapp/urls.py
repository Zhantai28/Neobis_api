from django.urls import path
from .views import ListCategory, DetailCategory, ListProduct, DetailProduct, \
    ListUser, DetailUser, ListComment, DetailComment, ListCart, DetailCart

urlpatterns = [
    path("categories/", ListCategory.as_view(), name="categorie"),
    path("categories/<int:pk>/", DetailCategory.as_view(),
         name="singlecategory"),
    path("products", ListProduct.as_view(), name="products"),
    path("products/<int:pk>/", DetailProduct.as_view(), name="singleproduct"),
    path("users", ListUser.as_view(), name="users"),
    path("users/<int:pk>/", DetailUser.as_view(), name="singleuser"),
    path("comments", ListComment.as_view(), name="comments"),
    path("comments/<int:pk>/", DetailComment.as_view(), name="singecomment"),
    path("carts", ListCart.as_view(), name="allcarts"),
    path("carts/<int:pk>", DetailCart.as_view(), name="cartdetail"),
    path("carts/<int:pk>/buy", DetailCart.as_view(), name="cartbuy"),
]
