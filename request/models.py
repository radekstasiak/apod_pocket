from django.db import models
from django.utils import timezone

MEDIA_TYPES = (
    ('image', 'Image'),
    ('video', 'Video'),
)


class Data(models.Model):
    title = models.CharField(max_length=150)
    created_date = models.DateField(default=timezone.now)
    url = models.URLField()
    hd_url = models.URLField(null=True, blank=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    explanation = models.TextField()
    concepts = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
