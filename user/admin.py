from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin

from django.contrib.auth.models import User

from .forms import UserCreationForm


class UserAdmin(OriginalUserAdmin):
    add_form = UserCreationForm

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return self.add_form
        return super().get_form(request, obj, **kwargs)


admin.site.unregister(User) # Unregister the original User admin because we need to do it to add new custom admin
admin.site.register(User, UserAdmin)