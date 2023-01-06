from django.contrib import admin
from .models import ChatRoom, Chat
from django.contrib.admin import ModelAdmin
from django.core.paginator import Paginator
from django.core.cache import cache


# Register your models here.

admin.site.register(ChatRoom)
admin.site.register(Chat)
