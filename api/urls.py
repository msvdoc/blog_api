from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


# Чтобы протестировать их, перейдите на http://127.0.0.1:8000/posts и создайте публикации. Я взял несколько статей из Медиума.
# Перейдите на один пост (например, http://127.0.0.1:8000/posts/1 и нажмите DELETE. Чтобы поменять название поста, обновите поле «title»
# и нажмите PUT.
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    # Объединение представлений с этими URL-паттернами создает эндпоинты:
    # get posts/,
    # post posts/,
    # get posts/<int:pk>/,
    # put posts/<int:pk>/
    # и delete posts/<int:pk>/.
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)