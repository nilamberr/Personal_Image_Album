from django.contrib import admin
from ImageApp.models import Images

# Register your models here.
@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display=('id','photo','post','date')