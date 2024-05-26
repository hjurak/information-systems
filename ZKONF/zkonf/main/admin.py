from django.contrib import admin
from .models import Area, ScientificWork, Participant, Conference, Presentation, Organizer, Organization

# Register all models
admin.site.register(Area)
admin.site.register(ScientificWork)
admin.site.register(Participant)
admin.site.register(Conference)
admin.site.register(Presentation)
admin.site.register(Organizer)
admin.site.register(Organization)
