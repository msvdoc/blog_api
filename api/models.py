from django.db import models



class Category(models.Model):
	name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Категория')
	owner = models.ManyToManyField('auth.User', related_name='categories', verbose_name='Автор')
	posts = models.ManyToManyField(Post, related_name='categories', verbose_name='Пост')
	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ['name']


class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	title = models.CharField(max_length=200, blank=True, default='', verbose_name='Название')
	body = models.TextField(blank=True, default='', verbose_name='Содержание')
	# Тип ForeignKey создает отношение многие-к-одному между текущей моделью и моделью, указанной в первом аргументе 
	# (auth.User — то есть, модель User, с которой вы работаете
	# Аргумент related_name позволяет задать другое имя доступа к текущей модели (posts) вместо стандартного (post_set).
	# Список постов будет добавлен в сериализатор User на следующем шаге для завершения отношения многие-к-одному.
	owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, verbose_name='Владелец')
	category = models.ManyToManyField(Category, verbose_name='Категория')

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
		ordering = ['created']

	def __str__(self):
		return self.title


# Комментарий — это текст, который пользователь добавляет в ответ на пост другого пользователя. К одному можно оставить несколько комментариев,
# а у поста может быть несколько комментариев от разных пользователей. Это значит, что нужно настроить две пары отношений многие-к-одному:
# между комментариями и пользователями, а также между комментариями и постами.
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    body = models.TextField(blank=False, verbose_name='Текст комментария')
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE, verbose_name='Пост')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created']

