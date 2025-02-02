from django.contrib import admin

# Register your models here.
from project_app.models import Module, Project,models
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display =['name','describe','status','create_time',id]

class ModuleAdmin(admin.ModelAdmin):
    list_display =['name','describe','create_time','project',id]


admin.site.register(Project,ProjectAdmin)
admin.site.register(Module,ModuleAdmin)