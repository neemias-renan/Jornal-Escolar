from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Edition, News, Comment, Profile

class NewsInline(admin.TabularInline):
    model = News
    extra = 0

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    extra = 0

class UserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    extra = 0

class EditionAdmin(admin.ModelAdmin):
    inlines = [NewsInline]
    extra = 0

class NewsAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    extra = 0

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Edition, EditionAdmin)
admin.site.register(News, NewsAdmin)