from django.contrib import admin

from accounts.models import UserProfile


@admin.register(UserProfile)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user',)

