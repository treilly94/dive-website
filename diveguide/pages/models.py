import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Location(models.Model):
    location_name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default='', blank=True)
    WATER_CHOICES = (('FW', 'Fresh water'), ('SW', 'Salt water'))
    water = models.CharField(max_length=2, choices=WATER_CHOICES, default='SW')
    address = models.CharField(max_length=200, default='', blank=True)
    google_place_id = models.CharField(max_length=100, default='')
    contact_phone = models.CharField(max_length=20, default='', blank=True)
    contact_email = models.EmailField(max_length=200, default='', blank=True)
    contact_website = models.CharField(max_length=200, default='', blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location_name

    def was_updated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.last_updated <= now
    was_updated_recently.admin_order_field = 'last_updated'
    was_updated_recently.boolean = True
    was_updated_recently.short_description = 'Updated recently?'
