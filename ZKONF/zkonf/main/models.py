# main/models.py

from django.db import models

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class ScientificWork(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    year_of_publication = models.IntegerField()
    areas = models.ManyToManyField(Area, related_name='works')
    def __str__(self):
        return self.title

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    works = models.ManyToManyField(ScientificWork, related_name='participants')

class Conference(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    year = models.IntegerField()

class Presentation(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    location = models.CharField(max_length=255)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    scientificwork = models.ForeignKey(ScientificWork, on_delete=models.CASCADE)

class Organizer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
