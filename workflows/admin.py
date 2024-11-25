from django.contrib import admin
from .models import Workflow

class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('name', 'use_case', 'version', 'created_at', 'updated_at', 'diagram_data_display')
    search_fields = ('name', 'use_case__title', 'version')
    list_filter = ('use_case', 'version')
    ordering = ('-created_at',)

    # Display JSON data as readable format in the admin list
    def diagram_data_display(self, obj):
        return str(obj.diagram_data)[:50]  # Limit the display to first 50 chars
    diagram_data_display.short_description = 'Diagram Data Preview'

    # Customize the form layout
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'use_case', 'diagram_data', 'version')
        }),
    )

    # Make timestamps read-only
    readonly_fields = ('created_at', 'updated_at')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # If the object is already created
            return ['version', 'created_at', 'updated_at']
        return ['created_at', 'updated_at']

# Register Workflow model in the Django admin
admin.site.register(Workflow, WorkflowAdmin)
