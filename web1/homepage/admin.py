from django.contrib import admin
from .models import Custom
from .models import Event   # Event modelini içe aktar

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "attendee_email", "start_time","time")  # Admin tablosunda gösterilecek alanlar

# Register your models here.
admin.site.register(Custom)
