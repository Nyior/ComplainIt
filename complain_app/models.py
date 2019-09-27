from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django.utils.translation import gettext

# Create your models here.

class Post(models.Model):  #this models a blog post in the databse
    author = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    body = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='post_pics')

    def __str__(self):
        return self.title
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    

class MinedData(models.Model): #this models a data that would be generated by the system's machine learning algorithm
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='mined_data')

    def __str__(self):
        return self.title
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class State(models.Model): #this models a Nigerian state in the databse
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Lga(models.Model): #this models a local government area under a Nigerian state in the databse
    name = models.CharField(max_length = 50)
    state = models.ForeignKey(State, on_delete = models.CASCADE) #one to many relationship, where one state could have many lga's

    def __str__(self):
        return self.name

class Agencies(models.Model): #this models a Nigerian security agency; police, ndlea, frsc, efcc in the databse
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    state = models.ManyToManyField(State)  #many to many relationship where a state could have many agencies and an agency could
                                            #exist in many states.
    def __str__(self):
        return self.name

class Category(models.Model): #this models a type of crime; arson, battery, murder etc in the databse
    name = models.CharField(max_length = 50) 
    
    def __str__(self):
        return self.name



class Status(models.Model): #this models the status of a reported crime in the databse
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Complain(models.Model): #this models a complaint logged by a user of the system in the databse
    passcode = models.CharField(max_length = 100)
    state = models.ForeignKey(State, on_delete = models.CASCADE)
    agency = models.ForeignKey(Agencies, on_delete = models.CASCADE)
    description = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    crime_type = models.ForeignKey(Category, on_delete = models.CASCADE)
    status = models.ForeignKey(Status, on_delete = models.CASCADE) #I NEED TO ADD AN LGA FIELD HERE.
    
    def __str__(self):
        return "{} at {}".format(self.crime_type, self.state)

    def get_absolute_url(request):
        return reverse('complain-create')
   
    


