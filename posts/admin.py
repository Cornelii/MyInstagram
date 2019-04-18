from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['content','image']}),
        ('Users', {'fields':['user','like_users']}),
    ]
    inlines = [CommentInline]
    search_fields = ['content']
    list_display =['user','content']
    

admin.site.register(Post, PostAdmin)
