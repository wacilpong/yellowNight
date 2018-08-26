from django.db import models
import sqlite3

# Create your models here.
class Realtimedata(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()

    def __select__(self):
        return self.title + '(' + self.link + ')'