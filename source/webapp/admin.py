from django.contrib import admin
from webapp.models import Client, Department, ClientInDep, LegalEntity


class DepartmentClientInline(admin.TabularInline):
    model = ClientInDep
    fields = ('client', 'department')
    list_display = ("client", "department", "created_at")

    extra = 1


class DepartmentAdmin(admin.ModelAdmin):
    inlines = (DepartmentClientInline,)
    list_display = ("identity_number", "name", "parent", "client_counts")

    @staticmethod
    def client_counts(obj):
        return obj.clients.count()


admin.site.register(LegalEntity)
admin.site.register(Client)
admin.site.register(Department, DepartmentAdmin)
# admin.site.register(Department, DepartmentlistAdmin)
