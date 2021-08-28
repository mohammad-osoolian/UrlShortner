from django.db import models


class Url(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField()
    key = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

