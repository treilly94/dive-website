import datetime
from django.db import models
from django.utils import timezone


class Location(models.Model):
    # Basics
    location_name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default='', blank=True)
    # Site details
    WATER_TYPES = (('FW', 'Fresh water'), ('SW', 'Salt water'))
    water_type = models.CharField(max_length=2, choices=WATER_TYPES, default='SW')
    WATER_ACCESS = (('RA', 'Ramp'), ('ST', 'Stairs'), ('LA', 'Ladder'), ('BO', 'Boat'))
    water_access = models.CharField(max_length=2, choices=WATER_ACCESS, default='RA')
    parking_cost = models.CharField(max_length=15, default='Free', blank=True)
    dive_cost = models.CharField(max_length=15, default='Free', blank=True)
    MEDICAL = (('Y', 'Yes'), ('N', 'No'))
    medical = models.CharField(max_length=2, choices=MEDICAL, default='N')
    # Location details
    address = models.CharField(max_length=200, default='', blank=True)
    latitude = models.CharField(max_length=10, default='')
    longitude = models.CharField(max_length=10, default='')
    metoffice_id = models.CharField(max_length=100, default='', blank=True)
    google_place_id = models.CharField(max_length=100, default='')
    # Contact details
    contact_phone = models.CharField(max_length=20, default='', blank=True)
    contact_email = models.EmailField(max_length=200, default='', blank=True)
    contact_website = models.URLField(max_length=200, default='', blank=True)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location_name

    def was_updated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.last_updated <= now
    was_updated_recently.boolean = True
    was_updated_recently.short_description = 'Updated recently?'

    def free_parking(self):
        if self.parking_cost == 'Free':
            return True
        else:
            return False
    free_parking.boolean = True
    free_parking.short_description = 'Free parking'

    def free_dive(self):
        if self.dive_cost == 'Free':
            return True
        else:
            return False
    free_dive.boolean = True
    free_dive.short_description = 'Free diving'
