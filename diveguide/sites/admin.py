from django.contrib import admin

from .models import Location


class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['location_name',
                                            'description']
                                 }
         ),
        ('Site details',        {'fields': ['water_type',
                                            'water_access',
                                            'parking_cost',
                                            'dive_cost',
                                            'medical']
                                 }
         ),
        ('Location details',    {'fields': ['address',
                                            'latitude',
                                            'longitude',
                                            'google_place_id',
                                            'metoffice_id']
                                 }
         ),
        ('Contact details',     {'fields': ['contact_phone',
                                            'contact_email',
                                            'contact_website']
                                 }
         )
    ]
    list_display = ('location_name',
                    'last_updated',
                    'was_updated_recently',
                    'free_parking',
                    'free_dive')
    list_filter = ['water_type']
    search_fields = ['location_name']


admin.site.register(Location, LocationAdmin)
