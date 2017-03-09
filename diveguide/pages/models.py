from django.db import models


class Site(models.Model):
    WATER_TYPES = (
        ('S', 'Salt'),
        ('F', 'Fresh'),
        )
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    water_type = models.CharField(max_length=1, choices=WATER_TYPES)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
