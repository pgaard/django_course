from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    something = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(null=True)
    organizer_email = models.EmailField(null=True)
    image = models.ImageField(upload_to='images') # just the path to a file, not the data
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True)
    participants = models.ManyToManyField(Participant, blank=True) # blank says admin field can be empty. makes pivot table

    # set name in the admin
    def __str__(self):
        return f'{self.title}'