from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    favorites = models.ManyToManyField('Article', blank=True, related_name='favored_by', verbose_name='Избранное')

    def __str__(self):
        return self.name


class Article(models.Model):
    user = models.ForeignKey(User, related_name='articles', on_delete=models.PROTECT, verbose_name='Пользователь')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=3000, verbose_name='Текст')
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return "%s.%s" % (self.pk, self.title)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.PROTECT, verbose_name='Пользователь')
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.PROTECT, verbose_name='Статья')
    text = models.TextField(max_length=1000, verbose_name='Текст')
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    parent_comment = models.ForeignKey('self', blank=True, null=True, related_name='comments', on_delete=models.PROTECT,
                                       verbose_name='Комментарий')

    def __str__(self):
        return "%s: %s - %s" % (self.article.title, self.user.name, self.text)


class Rating(models.Model):
    RATING_AWFUL = 'awful'
    RATING_BAD = 'bad'
    RATING_NORMAL = 'normal'
    RATING_GOOD = 'good'
    RATING_EXCELLENT = 'excellent'

    RATING_CHOICES = (
        (RATING_AWFUL, 'Ужасно'),
        (RATING_BAD, 'Плохо'),
        (RATING_NORMAL, 'Нормально'),
        (RATING_GOOD, 'Хорошо'),
        (RATING_EXCELLENT, 'Отлично')
    )

    user = models.ForeignKey(User, related_name='rate_article', on_delete=models.PROTECT, verbose_name='Пользователь')
    article = models.ForeignKey(Article, related_name='rate_article', on_delete=models.PROTECT, verbose_name='Статья')
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=20, choices=RATING_CHOICES, default=RATING_NORMAL, verbose_name='Оценка')

    def __str__(self):
        return "%s.%s -  %s" % (self.article.pk, self.article.title, self.status)
