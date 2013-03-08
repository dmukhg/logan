from django.db import models

class Event(models.Model):
  when = models.DateTimeField(auto_now=True)
  what = models.TextField()
