from django.db import models


class Sneaker(models.Model):
    label = models.CharField(max_length=240, blank=True, null=True)
    info = models.CharField(max_length=240, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    feature = models.ImageField(upload_to="predict/")

    def __str__(self):
        return self.label

    def __unicode__(self):
        return unicode(self.label)
