from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello you have located the HelloContacts index page, welcome!")

class ContactsList(TemplateView):
    template_name = "ContactsApp/templates/Contact/contacts_list.html"