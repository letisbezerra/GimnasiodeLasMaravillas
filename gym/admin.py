from django.contrib import admin
from gym.models import Instructor, Activity

# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('type', 'instructor', 'time', 'price')
    ordering = ("type",)
    search_fields = ("type", "instructor")

admin.site.register(Instructor)
admin.site.register(Activity, ActivityAdmin) 


