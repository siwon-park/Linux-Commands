from django.contrib import admin

from skills.models import Knowledge, Type, Skill

admin.site.register(Type)
admin.site.register(Skill)
admin.site.register(Knowledge)

