from django.db import models


class Pet(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    history = models.TextField(blank=False, null=False)
    photo = models.URLField(blank=False, null=False)
