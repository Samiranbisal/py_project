# from django.contrib import admin
# from services.models import services
# class serviceaAdmin(admin.ModelAdmin):
#     list_display = ('sservices_icon','services_title','services_das')
# admin.site.register(services,serviceaAdmin)

# Register your models here.

from django.contrib import admin
from services.models import Service  # Ensure the import reflects the new model name

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('services_icon', 'services_title', 'services_das')

admin.site.register(Service, ServiceAdmin)
