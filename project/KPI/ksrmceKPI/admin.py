# admin.py
from django.contrib import admin
from .models import Profile
from .models import KPI

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'designation', 'department', 'faculty_id')

admin.site.register(Profile, ProfileAdmin)


@admin.register(KPI)
class KPIAdmin(admin.ModelAdmin):
    list_display = ('name_of_author', 'title_of_article', 'published', 'indexed')
    search_fields = ('name_of_author', 'title_of_article', 'name_of_journal')
    list_filter = ('published', 'indexed')



