from django.contrib import admin

from .models import Curriculum, Version, Unit, Lesson, Reading


admin.site.register(Curriculum)
admin.site.register(Version)
admin.site.register(Unit)
admin.site.register(Lesson)
admin.site.register(Reading)
