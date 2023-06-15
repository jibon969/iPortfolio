from django.contrib import admin
from .models import Project, AboutSkill
from django_summernote.admin import SummernoteModelAdmin


@admin.register(AboutSkill)
class YourModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']

    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)
