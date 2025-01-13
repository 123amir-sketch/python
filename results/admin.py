from django.contrib import admin
from .models import ResultFile, Result
# Register your models here.
admin.site.register(ResultFile)
@admin.register(Result)
class registermodel(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'student_class', 'marks']
