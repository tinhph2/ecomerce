from django.contrib import admin

# Register your models here.

from .models import DemoUser

@admin.register(DemoUser)
class DemoUserAdmin(admin.ModelAdmin):
   list_display = ["id", "userName","passWord"]
   list_display_links =["userName"]
   list_per_page= 5
   list_filter = ["userName"]