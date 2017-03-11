from django.db import models


class Sneaker(models.Model):
    label = models.CharField(max_length=240)
    feature = models.URLField()

    def __str__(self):
        return self.label

    def __unicode__(self):
        return unicode(self.label)


class PredictSneaker(models.Model):
    feature = models.ImageField()
    label = models.CharField(max_length=240, blank=True, null=True)
