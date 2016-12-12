from django.db import models

# Create your models here.
class Interest(models.Model):
    InterestName = models.CharField(max_length = 15)
    InterestCode = models.CharField(max_length = 5)

class Relationship(models.Model):
    RelationshipName = models.CharField(max_length = 15)

class Contact(models.Model):
    DtAdded = models.DateField('Date Added')
    Title = models.CharField(max_length = 5)
    FirstName = models.CharField(max_length = 25)
    LastName = models.CharField(max_length = 30)
    EmailAddress = models.EmailField
    Interests = models.ManyToManyField(Interest)
    Relationship = models.OneToOneField(Relationship)

