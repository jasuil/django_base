from django.db import models

# Create your models here.
class Hello(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    create_at = models.DateTimeField('date published')