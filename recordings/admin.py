from django.contrib import admin
from .models import Record, Category, Author, Tag


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class RecordAdmin(admin.ModelAdmin):
    exclude = ('publishDate', )
    list_display = ('id', 'title', 'recordingDate')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Author, AuthorAdmin)