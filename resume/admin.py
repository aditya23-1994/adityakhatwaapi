from django.contrib import admin
from .models import Resume, Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'discription','created_at', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Resume)