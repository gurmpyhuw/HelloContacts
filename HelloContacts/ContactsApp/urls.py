from django.conf.urls import url

from . import views
#from templates.Contact import contacts_list

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Contact pages
    # url(r'^contactslist$', contacts_list.as_view(), name="contacts_list"),
]