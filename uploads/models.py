from django.core.files.storage import FileSystemStorage
from django.db import models

fs_one = FileSystemStorage(location='/home/adminsm/new1')
fs_two = FileSystemStorage(location='/home/adminsm/new2')
# fs_one = FileSystemStorage('/home/new')
# fs_two = FileSystemStorage('/home/new2')


class DocumentOne(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(storage=FileSystemStorage(location='/home/adminsm/new1', base_url='/home/adminsm/new1/'))
    uploaded_at = models.DateTimeField(auto_now_add=True)


class DocumentTwo(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(storage=FileSystemStorage(location='/home/adminsm/new2', base_url='/home/adminsm/new2/'))
    uploaded_at = models.DateTimeField(auto_now_add=True)
