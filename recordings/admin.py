# from django.contrib.auth.models import  BaseUserManager
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# from .models import CustomUser
from .models import Record, Category, Author, Tag

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('email', 'first_name', 'last_name',
#                     'is_staff', 'is_active',)
#     list_filter = ('email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff',
#          'is_superuser', 'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
#          ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError(_('The Email field must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class RecordAdmin(admin.ModelAdmin):
    exclude = ('publishDate', )
    list_display = ('id', 'title', 'recordingDate')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Author, AuthorAdmin)
