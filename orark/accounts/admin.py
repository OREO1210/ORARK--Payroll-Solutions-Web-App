from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .models import User
from django import forms


# Register your models here.

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserrAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name','gender','images')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'first_name', 'last_name', 'is_employee', 'is_hod','is_receptionist', 'is_active','gender','images')}
            ),
        )

    filter_horizontal = ()


admin.site.register(Employees)
admin.site.register(User,UserrAdmin)
admin.site.register(BaseSalary)
admin.site.register(ComplementarySalary)
admin.site.register(Dept)
admin.site.register(Designation)
