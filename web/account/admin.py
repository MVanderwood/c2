from django import forms
from django.contrib import admin
from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin
)
from django.utils.translation import (
    gettext,
    gettext_lazy as _,
)
from .models import (
    User,
    Email,
    Phone,
    Gender,
    Race,
    Ethnicity,
    UserRaceEthnicity,
)


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        exclude = ['user']


class EmailInline(admin.TabularInline):
    classes = ("emails-inline")
    model = Email
    form = EmailForm


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        exclude = []


class PhoneInline(admin.TabularInline):
    classes = ['phone_inline']
    model = Phone
    form = PhoneForm


class UserRaceEthnicityForm(forms.ModelForm):
    class Meta:
        model = UserRaceEthnicity
        exclude = ['user']

    class Media:
        js = ("user_race_ethnicities_admin.js",)


class UserRaceEthnicityInline(admin.TabularInline):
    classes = ("user-race-ethnicity-inline",)
    model = UserRaceEthnicity
    form = UserRaceEthnicityForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'gender',
        'age',
    )

    readonly_fields = (
        'last_login',
        'username',
        'date_joined',
    )

    inlines = [
        EmailInline,
        PhoneInline,
        UserRaceEthnicityInline,
    ]

    fieldsets = (
        (
            _('Personal info'),
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'gender',
                    'date_of_birth',
                    'locations',
                )
            }
        ),
        (
            _('User info'),
            {
                'classes': (
                    'collapse',
                ),
                'fields': (
                    'username',
                    'password',
                )
            }
        ),
        (
            _('Permissions'),
            {
                'classes': (
                    'collapse',
                ),
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        ),
        (
            _('Important dates'),
            {
                'classes': (
                    'collapse',
                ),
                'fields': (
                    'last_login',
                    'date_joined',
                )
            }
        ),
    )


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'address',
        'active',
    )

    search_fields = (
        'address',
        'active',
    )


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number',
        'active',
    )

    search_fields = (
        'number',
        'active',
    )


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'gender',
        'referred_to_as',
    )
    search_fields = (
        'gender',
        'referred_to_as',
    )


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'race',
    )
    search_fields = (
        'race',
    )


@admin.register(Ethnicity)
class EthnicityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'race',
        'ethnicity',
    )

    search_fields = (
        'race',
        'ethnicity',
    )
