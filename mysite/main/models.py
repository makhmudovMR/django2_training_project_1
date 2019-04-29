from django.db import models

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=150)
    tutorial_content = models.TextField(blank=True)
    tutorial_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tutorial_title