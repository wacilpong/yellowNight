from django.db import models

# Create your models here.
class realtimedata(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()

    def select(self):
        return title + '(' + ling + ')'