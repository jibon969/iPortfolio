from django.contrib import admin
from .models import Project, AboutSkill,Resume
from django_summernote.admin import SummernoteModelAdmin


class AboutSkillAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ['title']


admin.site.register(AboutSkill, AboutSkillAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']

    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Resume


admin.site.register(Resume, ResumeAdmin)