from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin

from api.models import (
    User,
    StudentType,
    Student
)

admin.site.site_header = "Sponsor"

admin.site.register(User)
admin.site.register(StudentType)
admin.site.register(Student)
