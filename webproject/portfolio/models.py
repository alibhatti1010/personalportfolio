from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year = models.IntegerField()
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.degree

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class OwnerInfo(models.Model):
    name = models.CharField(max_length=100)
    intro = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
