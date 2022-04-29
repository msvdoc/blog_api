from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category


class PostSerializer(serializers.ModelSerializer):
	# ReadOnlyField — это класс, возвращающий данные без изменения. В этом случае он используется для возвращения поля username вместо 
	# стандартного id
	owner = serializers.ReadOnlyField(source='owner.username')
	# Отношения многие-к-одному между комментариями и постом.
	comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = Post
		fields = ['id', 'title', 'body', 'owner', 'categories']
# Создаю клас сериализатор
# Класс ModelSerializer генерирует поля сериализатора, которые основаны на соответствующих свойствах модели. Это значит,что не нужно вручную указывать все атрибуты
# для поля сериализации, поскольку они вытягиваются напрямую из модели. Этот сериализатор также создает простые методы create() и update().
# При необходимости их можно переписать.
class UserSerializer(serializers.ModelSerializer):
	# Дальше добавьте поле posts в UserSerializer. Отношение многие-к-одному между постами и пользователями определено моделью Post в прошлом шаге. 
	# Название поля (posts) должно быть равным аргументу related_field поля Post.owner. Замените posts на post_set (значение по умолчанию), 
	# если вы не задали значение related_field в прошлом шаге. PrimaryKeyRelatedField представляет список публикаций в этом отношении 
	# многие-к-одному (many=True указывает на то, что постов может быть больше чем один).
	# Если не задать read_only=True поле posts будет иметь права записи по умолчанию. Это значит, что будет возможность вручную задавать
	# список статей, принадлежащих пользователю при его создании. Вряд ли это желаемое поведение.
	# Обратите внимание на то, что список posts — это, по сути, список id. Вместо этого можно возвращать список URL с помощью HyperLinkModelSerializer
	posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	# Отношения многие-к-одному между комментариями и пользователем
	comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = User
		# __all__ - это добавить все поля.
		fields = ['id', 'username', 'posts', 'comments'] 


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
 	#Обратите внимание на то, что поле post не меняется. После добавления поля post в массив fields он будет сериализоваться по умолчанию 
 	#(согласно ModelSerializer). Это эквивалентно post=serializers.PrimaryKeyRelatedField(queryset=Post.objects.all()).
	#Это значит, что у поля post есть право на запись по умолчанию: при создании комментария настраивается, какому посту он принадлежит.
    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts', 'categories']