from django.contrib import admin

# Register your models here.

from .models import Post


# we can  pass tuple as ("id",) not this ==> ("Id")

admin.site.register(Post)

'''

# or
    


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "auther")


admin.site.register(Post, StudentAdmin)


'''
