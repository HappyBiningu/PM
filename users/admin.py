from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Admin for Profile model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'name', 'surname', 'phone_number', 'profile_picture')
    search_fields = ('user__username', 'name', 'surname', 'phone_number')
    list_filter = ('role',)
    ordering = ('user__username',)
    fieldsets = (
        (None, {
            'fields': ('user', 'role', 'name', 'surname', 'phone_number', 'profile_picture')
        }),
    )

    def save_model(self, request, obj, form, change):
        # Automatically set the 'user' if not provided
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

# Register Profile model in the Django admin
admin.site.register(Profile, ProfileAdmin)
