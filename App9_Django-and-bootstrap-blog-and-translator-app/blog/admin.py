from django.contrib import admin
from .models import Post


# For better display in admin window
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')

# Register your models here. (So when PostAdmin obj us added it will overwrite display data in admin window that comes from the Post obj)
admin.site.register(Post, PostAdmin)