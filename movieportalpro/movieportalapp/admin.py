from django.contrib import admin
from .models import Telugu,Hindi,English

class AdminTelugu(admin.ModelAdmin):
    list_display=["m_name","m_director","m_hero","m_heroine"]
class AdminHindi(admin.ModelAdmin):
    list_display =["m_name","m_director","m_hero","m_heroine"]
class AdminEnglish(admin.ModelAdmin):
    list_display = ["m_name","m_director","m_hero","m_heroine"]

admin.site.register(Telugu,AdminTelugu)
admin.site.register(English,AdminEnglish)
admin.site.register(Hindi,AdminHindi)
