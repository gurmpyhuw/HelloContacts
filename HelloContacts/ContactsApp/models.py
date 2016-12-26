from django.db import models

# Create your models here.
class Title(models.Model):
    Name = models.CharField(max_length = 10)

    def __str__(self):
        return self.Name 

class Region(models.Model):
    Name = models.CharField(max_length = 4)
    Description = models.CharField(max_length = 25)

    def __str__(self):
        return self.Name 

class Relationship(models.Model):
    Name = models.CharField(max_length = 25)

    def __str__(self):
        return self.Name 

class JobTitle(models.Model):
    Job_Name = models.CharField(max_length = 25)

    def __str__(self):
        return self.JobName 

class Type(models.Model):
    Type_Name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.TypeName 

class Interest(models.Model):
    Short_Name = models.CharField(max_length = 3)
    Full_Name = models.CharField(max_length = 25)

    def __str__(self):
        return self.ShortName 

class Source(models.Model):
    Type = models.ForeignKey(Type)
    Source = models.CharField(max_length = 50)
    Source_Info = models.CharField(max_length = 100)
    Interest = models.ForeignKey(Interest)

    def __str__(self):
        return self.Source 

class Contact(models.Model):
    DtAdded = models.DateField(verbose_name = 'Date Added')
    Title = models.ForeignKey(Title)
    First_Name = models.CharField(max_length = 25)
    Last_Name = models.CharField(max_length = 50)
    Email = models.EmailField()
    Region = models.ForeignKey(Region)
    Interests = models.ManyToManyField(Interest, blank=True)
    Relationship = models.ForeignKey(Relationship)
    JobTitle = models.ForeignKey(JobTitle)

    def __str__(self):
        return u'%s %s' % (self.FirstName, self.LastName) 