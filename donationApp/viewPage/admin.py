from django.contrib import admin
from .models import Picture, Project
from .forms import ProjectForm

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm

admin.site.register(Picture)
