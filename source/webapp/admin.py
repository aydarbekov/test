from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from webapp.models import Client, Department


class DepartmentClientInline(admin.TabularInline):
    model = Client
    fields = ('identity_number', 'first_name')
    extra = 1


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    ordering = ('-updated_at',)

    inlines = (DepartmentClientInline,)


admin.site.register(Client)
