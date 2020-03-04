from django.core.files.storage import FileSystemStorage
from django.db import models

fs_one = FileSystemStorage('/home/adminsm/new1')
fs_two = FileSystemStorage('/home/adminsm/new2')
# fs_one = FileSystemStorage('/home/new')
# fs_two = FileSystemStorage('/home/new2')


class DocumentOne(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(storage=fs_one)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class DocumentTwo(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(storage=fs_two)
    uploaded_at = models.DateTimeField(auto_now_add=True)
