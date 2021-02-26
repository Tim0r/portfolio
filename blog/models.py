from django.db import models
from django.db.models.base import Model


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def format_date(self):
        return self.pub_date.strftime('%b %e %Y')