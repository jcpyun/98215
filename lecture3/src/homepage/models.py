from __future__ import unicode_literals

from django.db import models

# Create your models here.

class blog(models.Model):
    title=models.CharField(max_length=100)
    context=models.TextField()
    after= models.DateTimeField()
    initial= models.DateTimeField()
    
    def __unicode__(self):   ### python 2.7
        return self.title 