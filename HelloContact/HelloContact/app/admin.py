from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from.models import *

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
        import_id_fields = ('email',)
        exclude = ('id',)

class InterestResource(resources.ModelResource):
    class Meta:
        model = Interest

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('title', 'first_name', 'last_name', 'email', 'list_of_interests')
    def list_of_interests(self, obj):
        return("%s" % ', '.join([interest.short_name for interest in obj.interests.all()]))
    list_of_interests.short_description = 'Contact interests'
    list_filter = (('region',admin.RelatedOnlyFieldListFilter),('relationship',admin.RelatedOnlyFieldListFilter),('interests',admin.RelatedOnlyFieldListFilter),)
    filter_horizontal = ('interests',)
    list_per_page = 10
    resource_class = ContactResource

class InterestAdmin(ImportExportModelAdmin):
    list_display = ('short_name','full_name',)
    ordering = ('short_name',)
    resource_class = InterestResource

admin.site.register(Title)
admin.site.register(Region)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Type)
admin.site.register(Relationship)
admin.site.register(JobTitle)
admin.site.register(Source)