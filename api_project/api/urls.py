from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList  # Import both views
from rest_framework.authtoken.views import obtain_auth_token


# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
     path('', include(router.urls)),
      path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token retrieval endpoint
]