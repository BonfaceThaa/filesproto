from django.core.files.storage import FileSystemStorage
from django.db import models

BASE_PATH = '/home/adminsm/'


class DocumentOne(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(storage=FileSystemStorage(location=BASE_PATH + '/new1', base_url=BASE_PATH + '/new1/'))
    uploaded_at = models.DateTimeField(auto_now_add=True)


class DocumentTwo(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(storage=FileSystemStorage(location=BASE_PATH + '/new2', base_url=BASE_PATH + '/new2/'))
    uploaded_at = models.DateTimeField(auto_now_add=True)
