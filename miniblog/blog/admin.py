from django.contrib import admin

# Register your models here.
from .models import Blogger, Post, Comment

#admin.site.register(Blogger)
#admin.site.register(Post)
#admin.site.register(Comment)

# Define the admin class
class BloggerAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Blogger, BloggerAdmin)


# Register the Admin classes for BookInstance using the decorator
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author','post_time')
    list_filter =('post','author')

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','post_date')
    list_filter = ('title','author','post_date')    

    inlines =[CommentInline]