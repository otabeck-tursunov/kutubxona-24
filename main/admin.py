from django.contrib import admin
from .models import *


class TalabaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'guruh', 'kurs', 'kitob_soni',)
    list_display_links = ('id', 'ism')
    list_filter = ('guruh', 'kurs')
    list_per_page = 50
    list_editable = ('kitob_soni',)
    search_fields = ('ism', 'guruh')
    search_help_text = "Ism va guruh bo'yicha qidiring!"


class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1


class MuallifAdmin(admin.ModelAdmin):
    list_display = ('ism', 'jins', 't_sana', 'kitob_soni', 'tirik',)
    inlines = (KitobInline,)


class RecordAdmin(admin.ModelAdmin):
    date_hierarchy = 'olingan_sana'


admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Kutubxonachi)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Kitob)
admin.site.register(Record, RecordAdmin)
