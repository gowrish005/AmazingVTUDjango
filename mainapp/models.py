from django.db import models

class PageView(models.Model):
    page_name = models.CharField(max_length=100, unique=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.page_name}: {self.view_count} views"

class Semester(models.Model):
    name = models.IntegerField()  # e.g., "1st Semester"

class Branch(models.Model):
    name = models.CharField(max_length=50)  # e.g., "CSE"
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)

class Subject(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Computer Networks"
    subjectcode = models.CharField(max_length=10)  # e.g., "CS  601"
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)

class Module(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Module 1"
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField(upload_to='files/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TempModule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='temp_images/', null=True, blank=True)
    file = models.FileField(upload_to='temp_files/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TempBranch(models.Model):
    name = models.CharField(max_length=50)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TempSubject(models.Model):
    name = models.CharField(max_length=100)
    subjectcode = models.CharField(max_length=10)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name