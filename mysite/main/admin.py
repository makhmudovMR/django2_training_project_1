from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries
from tinymce.widgets import TinyMCE
from django.db import models

class TutorialAdmin(admin.ModelAdmin):
    # отображение полей при редактировании или добавлении
    # fields = ['tutorial_title', 'tutorial_content', 'tutorial_published']

    # Отображение полей секциями
    fieldsets = [
        ('Title/date/slug', {'fields': ['tutorial_title', 'tutorial_published', 'tutorial_slug', 'tutorial_series']}),
        ('Content', {'fields': ['tutorial_content']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)