from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Section(models.Model):
    section_name = models.CharField(max_length=30)

    def __str__(self):
        return self.section_name


class Subject(models.Model):
    subject_name = models.CharField(max_length=40)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name


class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    file_name = models.FileField(upload_to='media/', default='media/myfile.pdf')
    date_posted = models.DateTimeField(default=timezone.now)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.file_name)










