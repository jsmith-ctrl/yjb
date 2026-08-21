from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, EmployeeProfile, EmployerProfile


@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "available_for_work",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
    )


@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "company_name",
        "position",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
        "company_name",
    )

class EmployeeProfileInline(admin.StackedInline):
    model = EmployeeProfile
    extra = 0
    can_delete = False


class EmployerProfileInline(admin.StackedInline):
    model = EmployerProfile
    extra = 0
    can_delete = False

@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
        "is_active",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Information",
            {
                "fields": (
                    "role",
                    "birth_date",
                    "phone",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Information",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "role",
                    "birth_date",
                    "phone",
                )
            },
        ),
    )

    def get_inlines(self, request, obj):
        if obj is None:
            return []

        if obj.role == User.Role.EMPLOYEE:
            return [EmployeeProfileInline]

        if obj.role == User.Role.EMPLOYER:
            return [EmployerProfileInline]

        return []