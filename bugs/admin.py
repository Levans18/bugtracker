from django.contrib import admin
from .models import Bug

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'severity', 'created_at')
    list_filter = ('status', 'severity')
    search_fields = ('title', 'description')