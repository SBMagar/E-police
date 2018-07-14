from django.db import models
from django.contrib.auth.models import User

class Userdata(models.Model):
    user = models.OneToOneField(User)
    email = models.CharField(max_length=40, unique=True)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    phone = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    dob = models.DateField('Date of Birth')
 
    def __str__(self):              # __unicode__ on Python 2
        return self.email

class VoterModel(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    vid = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    dob = models.DateField('Date of Birth')

    def __str__(self):
        return self.vid

class PasModel(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    pid = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    dob = models.DateField('Date of Birth')

    def __str__(self):
        return self.pid

class LcnModel(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    lid = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    dob = models.DateField('Date of Birth')

    def __str__(self):
        return self.lid

class CtzModel(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    cid = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    dob = models.DateField('Date of Birth')

    def __str__(self):
        return self.cid