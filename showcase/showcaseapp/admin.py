from django.contrib import admin
from .models import Word, Language


class WordAdmin(admin.ModelAdmin):
    fields = ["word_text", "language", "example_usage"]
    readonly_fields = ["example_usage",]


admin.site.register(Word, WordAdmin)
admin.site.register(Language)
