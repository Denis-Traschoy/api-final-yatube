from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    '''Я немного не понял, в исходнике этой модели нет, но в статичной
    документации запросы к этой модели есть, в самом задании просили
    только Follow добавить, если эта модель не нужна то я ее делитну,
    но тогда не совсем понимаю к чему мне запрос по группам делать.'''
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower_set'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following_set'
    )

    class Meta:
        unique_together = ('user', 'following')
        constraints = [
            models.CheckConstraint(
                condition=~models.Q(user=models.F('following')),
                name='cannot_follow_self'
            )
        ]

    def __str__(self):
        return f'{self.user.username} подписан на {self.following.username}'
