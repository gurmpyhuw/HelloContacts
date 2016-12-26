from django.contrib import admin

from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('Title', 'First_Name', 'Last_Name')
    #def list_of_interests(self, obj):
    #    return("%s" % ', '.join([Interest.Short_Name for interest in obj.Interests.all()]))
    #list_of_interests.short_description = 'Contact interests'


# Register your models here.
admin.site.register(Title)
admin.site.register(Region)
admin.site.register(Interest)
admin.site.register(Contact)
admin.site.register(Type)
admin.site.register(Relationship)
admin.site.register(JobTitle)
admin.site.register(Source)