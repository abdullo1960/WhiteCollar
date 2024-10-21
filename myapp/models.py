
from django.db import models
from myapp.general.models import BaseModel

class Info(BaseModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.title}"
    
class Contact(BaseModel):
    name = models.CharField(max_length=36)
    email = models.CharField(max_length=36)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    year = models.DateField(null=True, blank=True)
    hour = models.TextField(null=True, blank=True)
    text = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.name}: {self.email}: {self.text}"
    
    
class BlogModel(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    when_created = models.CharField(max_length=36)
    by_who = models.CharField(max_length=36)
    tarif = models.CharField(max_length=36)

    def __str__(self):
        return f"{self.name}"
    
class MessageModel(BaseModel):
    name = models.CharField(max_length=36)
    email = models.CharField(max_length=36)
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=36)
    text = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.name}--{self.email}--{self.text}"
    
    
class Testimonial(BaseModel):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name}: write {self.description}"


class ExpertsModel(BaseModel):
    title = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.title}"
    
    
class DataModel(BaseModel):
    text = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.text}"

class EmailModel(BaseModel):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.email}"
    
class LocationModel(BaseModel):
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.location}"