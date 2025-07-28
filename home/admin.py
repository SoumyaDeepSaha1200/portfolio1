from django.contrib import admin
from .models import *

class StaticImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'static_path', 'alt_text')
admin.site.register(AboutImage, StaticImageAdmin)
admin.site.register(ServiceCard)
admin.site.register(ProjectCard)
admin.site.register(WebDevProjectCard)
admin.site.register(AppDevProjectCard)
admin.site.register(PythonDevProjectCard)
admin.site.register(UIUXProjectCard)
admin.site.register(AchivementCard)
admin.site.register(AchivementCardModel)
admin.site.register(certificate)
admin.site.register(blog)
