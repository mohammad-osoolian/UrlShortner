from django.db import models, reset_queries
from .feeds import URLGenerator


class Url(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField()
    key = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            super().save(*args, **kwargs)
            geneator = URLGenerator()
            self.key = geneator.generate_unique_key(self.id)
        return super().save(*args, **kwargs)
        
 