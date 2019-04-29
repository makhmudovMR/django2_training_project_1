from django.db import models
from datetime import datetime
# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=150)
    tutorial_content = models.TextField(blank=True)
    tutorial_published = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.tutorial_title