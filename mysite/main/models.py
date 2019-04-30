from django.db import models
from datetime import datetime
from time import time
from django.utils.text import slugify


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

# Create your models here.


class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=150)
    category_summary = models.CharField(max_length=150)
    category_slug = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.category_slug = gen_slug(self.tutorial_category)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.tutorial_category


class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey('TutorialCategory', verbose_name='Category', on_delete=models.CASCADE)
    series_summary = models.CharField(max_length=200)

    def __str__(self):
        return self.tutorial_series


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=150)
    tutorial_slug = models.CharField(max_length=200, blank=True)
    tutorial_content = models.TextField(blank=True)
    tutorial_published = models.DateTimeField(default=datetime.now())
    tutorial_series = models.ForeignKey('TutorialSeries', on_delete=models.CASCADE, verbose_name='Series')

    def save(self, *args, **kwargs):
        if not self.id:
            self.tutorial_slug = gen_slug(self.tutorial_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tutorial_title