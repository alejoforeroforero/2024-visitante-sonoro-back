from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


admin.site.register(CustomUser, CustomUserAdmin)

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'birth_date', 'phone_number', 'google_id', 'google_picture', 'profile_picture']
#     list_filter = ['is_staff', 'is_superuser', 'is_active', 'groups']
#     search_fields = ['username', 'first_name', 'last_name', 'email']
#     ordering = ['username']
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'birth_date', 'phone_number', 'address', 'favorite_records')}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )

#     fieldsets = UserAdmin.fieldsets + (
#         ('Profile Picture', {'fields': ('profile_picture',)}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'birth_date', 'phone_number', 'address'),
#         }),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ('Profile Picture', {'fields': ('profile_picture',)}),
#     )

# admin.site.register(CustomUser, CustomUserAdmin)