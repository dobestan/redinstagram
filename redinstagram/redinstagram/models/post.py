from django.db import models


class PostManager(models.Manager):
    pass


class Post(models.Model):

    provider_hash_id = models.CharField(
        max_length=16,
        unique=True,
        verbose_name='인스타그램 ID',
    )
    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

    content = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='원본 이미지 URL',
    )
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name='이미지',
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    objects = PostManager()

    class Meta:
        verbose_name = '포스트'
        verbose_name_plural = verbose_name

        ordering = ['-created_at', ]
        get_latest_by = 'created_at'

    def _create_hash_id(self):
        from redinstagram.utils.hashids import get_encoded_hashid

        self.hash_id = get_encoded_hashid(self)
        self.save()
