from django.contrib import admin

from .models import Question, Choice, Location

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['location_name',
                                            'description']}),
        ('Site details',        {'fields': ['water_type',
                                            'water_access',
                                            'parking_cost',
                                            'dive_cost',
                                            'medical']}),
        ('Location details',    {'fields': ['address',
                                            'latitude',
                                            'longitude',
                                            'google_place_id',
                                            'metoffice_id']}),
        ('Contact details',     {'fields': ['contact_phone',
                                            'contact_email',
                                            'contact_website']}),
    ]
    list_display = ('location_name', 'last_updated', 'was_updated_recently', 'is_free')
    list_filter = ['water_type']
    search_fields = ['location_name']

admin.site.register(Location, LocationAdmin)
