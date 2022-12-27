from django.contrib import admin
from .models import count
# Register your models here.

@admin.register(count)
class countAdmin(admin.ModelAdmin):
    list_display = ['likeCount', 'dislikeCount']