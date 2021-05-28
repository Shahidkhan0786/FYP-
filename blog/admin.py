from django.contrib import admin
from .models import Contact,post,Catagory
# Register your models here.
class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email']

class AdminCatagory(admin.ModelAdmin):
    list_display = ['id','catagory_name']


class Adminpost(admin.ModelAdmin):
    list_display = ['post_id','title']
    list_filter = ('status', 'timeStamp', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)



admin.site.register(post, Adminpost)

admin.site.register(Contact, AdminContact)
admin.site.register(Catagory, AdminCatagory)
