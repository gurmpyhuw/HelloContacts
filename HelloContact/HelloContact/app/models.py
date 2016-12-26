"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Title(models.Model):
    name = models.CharField(max_length = 10)

    def __str__(self):
        return self.name 

class Region(models.Model):
    name = models.CharField(max_length = 4)
    description = models.CharField(max_length = 25)

    def __str__(self):
        return self.name 

class Relationship(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self):
        return self.name 

class JobTitle(models.Model):
    job_name = models.CharField(max_length = 25)

    def __str__(self):
        return self.job_name 

class Type(models.Model):
    type_name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.type_name 

class Interest(models.Model):
    short_name = models.CharField(max_length = 35)
    full_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.short_name 

class Source(models.Model):
    type = models.ForeignKey(Type)
    source = models.CharField(max_length = 50)
    source_info = models.CharField(max_length = 100)
    interest = models.ForeignKey(Interest)

    def __str__(self):
        return self.source 

class Contact(models.Model):
    dt_added = models.DateField("Date Added")
    title = models.ForeignKey(Title)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    job_title = models.ForeignKey(JobTitle)
    region = models.ForeignKey(Region)
    interests = models.ManyToManyField(Interest, blank = True)
    relationship = models.ForeignKey(Relationship)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name) 