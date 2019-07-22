from django.contrib import admin
from .models import *


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic_name', 'file_name', 'uploaded_by', 'subject')
    list_display_links = ('id', 'topic_name')
    search_fields = ('topic_name', 'subject')
    list_per_page = 25


admin.site.register(Topic, PageAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'section_name')
    list_display_links = ('id', 'section_name')
    search_fields = ('section_name',)
    list_per_page = 25


admin.site.register(Section, PageAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_name')
    list_display_links = ('id', 'subject_name')
    search_fields = ('subject_name',)
    list_per_page = 25


admin.site.register(Subject, PageAdmin)
