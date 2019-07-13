from django.contrib import admin
from .models import Users
# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'age', 'phone', 'email']
    # 搜索字段
    search_fields = ['username', 'phone']
    # 过滤字段
    list_filter = ['username', 'phone']
    list_per_page = 2
admin.site.register(Users, UsersAdmin)