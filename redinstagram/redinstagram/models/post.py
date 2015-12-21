from django.db import models


class PostManager(models.Manager):
    pass


class Post(models.Model):

    content = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    objects = PostManager()

    class Meta:
        verbose_name = '포스트'
        verbose_name_plural = verbose_name

        ordering = ['-created_at', ]
        get_latest_by = 'created_at'
