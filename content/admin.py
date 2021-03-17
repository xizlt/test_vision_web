from django.contrib import admin
from .models import *


@admin.register(BlockReviewItem)
class BlockReviewItemAdmin(admin.ModelAdmin):
    fields = ('name', 'text', 'img', 'position')
    list_display = ('name', 'text', 'img', 'position')


@admin.register(IconStyle)
class IconStyleAdmin(admin.ModelAdmin):
    fields = ('icon_class',)
    list_display = ('icon_class',)


@admin.register(BlockAboutItem)
class BlockAboutItemAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


@admin.register(BlockTitleItem)
class BlockTitleItemAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


@admin.register(BlockTitle)
class BlockTitleAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'img', 'point')
    list_display = ('title', 'text', 'img')
    filter_horizontal = ('point',)


@admin.register(BlockAbout)
class BlockAboutAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'img', 'point')
    list_display = ('title', 'text', 'img')
    filter_horizontal = ('point',)


@admin.register(BlockSkill)
class BlockSkillAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'icon_class')
    list_display = ('title', 'text', 'icon_class')


@admin.register(BlockReviews)
class BlockTitleAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'img', 'point')
    list_display = ('title', 'text', 'img')
    filter_horizontal = ('point',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ('name', 'email')
    list_display = ('name', 'email')
