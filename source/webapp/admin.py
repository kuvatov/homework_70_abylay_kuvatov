from django.contrib import admin

from webapp.models import Issue, Type, Status


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = ['summary', 'description', 'status', 'created_at']
    list_filter = ['summary', 'status', 'created_at']
    search_fields = ['summary', 'status', 'type', 'created_at']
    fields = ['summary', 'description', 'status', 'created_at', 'edited_at']
    readonly_fields = ['created_at', 'edited_at']


class IssueTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'created_at']
    fields = ['name', 'created_at', 'edited_at']
    readonly_fields = ['created_at', 'edited_at']


class IssueStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'created_at']
    fields = ['name', 'created_at', 'edited_at']
    readonly_fields = ['created_at', 'edited_at']


admin.site.register(Issue, IssueAdmin)
admin.site.register(Type, IssueTypeAdmin)
admin.site.register(Status, IssueStatusAdmin)
