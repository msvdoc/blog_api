"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    # Для удобства добавим кнопку «Log in» в графическое представление API с помощью следующего кода в blog/urls.py:
    # Сейчас можно создать пост, будучи зарегистрированным, но для удаления или изменения данных этого не требуется — даже если пост вам 
    # не принадлежит. Попробуйте зайти под другим аккаунтом, и вы сможете удалить посты, принадлежащие admin.
    # Чтобы аутентифицировать пользователя и быть уверенным в том, что только владелец поста может обновлять и удалять его, 
    # нужно добавить другие разрешения.
    path('api-auth/', include('rest_framework.urls')),
]
