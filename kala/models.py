from django.db import models


class KalaList(models.Model):
    STATUS_CODE = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    status = models.CharField(choices=STATUS_CODE, max_length=3)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
