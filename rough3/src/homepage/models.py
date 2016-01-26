from __future__ import unicode_literals

from django.db import models

# Create your models here.
class blog(models.Model):
    title= models.CharField(max_length=120)
    content=models.TextField()
    updated= models.DateTimeField()
    timestamp= models.DateTimeField()
    
    def __unicode__(self):
        return self.title
