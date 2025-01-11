from django.db import models

# Create your models here.
# models.py
from django.db import models

class Year(models.Model):
    name = models.CharField(max_length=20)  # e.g., "1st Year"

class Branch(models.Model):
    name = models.CharField(max_length=50)  # e.g., "CSE"
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Computer Networks"
    subjectcode = models.CharField(max_length=10)  # e.g., "CS  601"
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

class Module(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Module 1"
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
