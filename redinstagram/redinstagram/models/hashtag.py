from django.db import models


class HashtagManager(models.Manager):
    pass


class Hashtag(models.Model):

    posts = models.ManyToManyField(
        'Post',
        blank=True,
    )

    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='이름',
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    objects = HashtagManager()

    class Meta:
        verbose_name = '해시태그'
        verbose_name_plural = verbose_name

        ordering = ['name', ]
        get_latest_by = 'created_at'

    def __str__(self):
        return self.name

    def update_posts(self):
        pass
