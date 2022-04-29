from django.shortcuts import render
# Код для того чтобы редактировать посты мого только авторизированный пользователь:
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
# =========================================================
from . import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category

# REST Framework предоставляет несколько обобщенных представлений, основанных на классе APIView. Они представляют собой самые распространенные 
# паттерны.Например, ListAPIView используется для эндпоинтов с доступом только для чтения. Он предоставляет метод-обработчик get. 
# ListCreateAPIView используется для эндпоинтов с разрешением чтения-записи, а также обработчики get и post. Для создания эндпоинта только
# для чтения, который возвращал бы список пользователей, добавляю следующее:
# ===================================================================================================================
# Названия представлений должны быть в следующем формате: {ModelName}List и {ModelName}Details для коллекции
# объектов и одного объекта соответственно
# ===========================================================================================================================
class UserList(generics.ListAPIView):
    # Данное представление будет выводить список пользователей.
    queryset = User.objects.all() 
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    # Данное представление будет выводить одного пользователя по id
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
# Create your views here.

# ListCreateAPIView и RetrieveUpdateDestroyAPIView предоставляют самые распространенные обработчики API-методов: get и post для списка 
# (ListCreateAPIView) и get, update и delete для одной сущности (RetrieveUpdateDestroyAPIView).
# Также нужно перезаписать функцию по умолчанию perform_create, чтобы задать поле owner текущего пользователя (значение self.request.user).
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    #Устанавливает разрешение на добавление, удаление, изменение постов только авторизированному пользователю (автору этих постов).
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    # Представлению PostList требуется разрешение IsAuthenticatedOrReadOnly, потому что пользователь должен аутентифицироваться, чтобы создать пост,
    # а вот просматривать список может любой пользователь. Для PostDetails нужны оба разрешения, поскольку обновлять или удалять пост должен только
    # залогиненный пользователь, а также его владелец. Для получения поста прав не нужно. Вернитесь на http://127.0.0.1:8000/posts. Зайдите в учетную
    # запись admin и другие, чтобы проверить, какие действия доступны аутентифицированным и анонимным пользователям. Будучи разлогиненным,
    # вы не должны иметь возможность создавать, удалять или обновлять посты. При аутентификации вы не должны иметь право удалять или редактировать
    # чужие посты.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]



class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]