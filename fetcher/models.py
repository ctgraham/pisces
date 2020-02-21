from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class FetchRun(models.Model):
    STARTED = 0
    FINISHED = 1
    ERRORED = 2
    STATUS_CHOICES = (
        (STARTED, 'Started'),
        (FINISHED, 'Finished'),
        (ERRORED, 'Errored'),
    )
    ARCHIVESSPACE = 0
    CARTOGRAPHER = 1
    SOURCE_CHOICES = (
        (ARCHIVESSPACE, 'ArchivesSpace'),
        (CARTOGRAPHER, 'Cartographer'),
    )
    ARCHIVESSPACE_OBJECT_TYPE_CHOICES = (
        ('resource', 'Resource'),
        ('archival_object', 'Archival Object'),
        ('subject', 'Subject'),
        ('person', 'Person'),
        ('organization', 'Organization'),
        ('family', 'Family'),
    )
    CARTOGRAPHER_OBJECT_TYPE_CHOICES = (
        ('arrangement_map', 'Arrangement Map'),
    )
    OBJECT_TYPE_CHOICES = ARCHIVESSPACE_OBJECT_TYPE_CHOICES + CARTOGRAPHER_OBJECT_TYPE_CHOICES
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    object_type = models.CharField(max_length=100, choices=OBJECT_TYPE_CHOICES, null=True, blank=True)


class FetchRunError(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=255)
    run = models.ForeignKey(FetchRun, on_delete=models.CASCADE)