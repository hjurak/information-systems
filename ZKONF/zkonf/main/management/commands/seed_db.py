# main/management/commands/seed_db.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from main.models import Area, ScientificWork, Participant, Conference, Presentation, Organizer, Organization

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Area.objects.all().delete()
        ScientificWork.objects.all().delete()
        Participant.objects.all().delete()
        Conference.objects.all().delete()
        Presentation.objects.all().delete()
        Organizer.objects.all().delete()
        Organization.objects.all().delete()

        # Seed Areas
        area1 = Area.objects.create(name='Računarstvo')
        area2 = Area.objects.create(name='Genetika')
        area3 = Area.objects.create(name='Robotika')

        # Seed ScientificWorks
        leo_satellites = ScientificWork.objects.create(title='LEO Satellites', authors='V. Petrov, A. Ivanov', year_of_publication=2022)
        cancer_genomics = ScientificWork.objects.create(title='Cancer Genomics', authors='D. Ostojić', year_of_publication=2022)
        robot_navigation = ScientificWork.objects.create(title='Robot Navigation', authors='R. Bauer, H. Sonntag, B. Hauser', year_of_publication=2022)
        leo_satellites.areas.set([area1])
        cancer_genomics.areas.set([area2])
        robot_navigation.areas.set([area3])

        # Seed Participants
        vasilij = Participant.objects.create(first_name='Vasilij', last_name='Petrov')
        davor = Participant.objects.create(first_name='Davor', last_name='Ostojić')
        silvia = Participant.objects.create(first_name='Silvia', last_name='Koch')
        vasilij.works.set([leo_satellites])
        davor.works.set([cancer_genomics])
        silvia.works.set([robot_navigation])

        # Seed Organizations
        org1 = Organization.objects.create(name='Organizacija evenata', country='Hrvatska')
        org2 = Organization.objects.create(name='Event Organisation', country='Njemačka')
        org3 = Organization.objects.create(name='Organizzazione di eventi', country='Italija')

        # Seed Organizers
        organizer1 = Organizer.objects.create(first_name='Marija', last_name='Jurić', organization=org1)
        organizer2 = Organizer.objects.create(first_name='Thomas', last_name='Schmidt', organization=org2)
        organizer3 = Organizer.objects.create(first_name='Francesca', last_name='Ricci', organization=org3)

        # Seed Conferences
        konferencija_u_zagrebu = Conference.objects.create(name='Konferencija u Zagrebu', year=2023)

        # Seed Presentations
        Presentation.objects.create(time=timezone.now(), location='Zagreb', conference=konferencija_u_zagrebu, participant=vasilij, scientificwork=leo_satellites)
        Presentation.objects.create(time=timezone.now(), location='Zagreb', conference=konferencija_u_zagrebu, participant=davor, scientificwork=cancer_genomics)
        Presentation.objects.create(time=timezone.now(), location='Zagreb', conference=konferencija_u_zagrebu, participant=silvia, scientificwork=robot_navigation)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
