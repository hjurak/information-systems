from django.test import TestCase, Client
from django.urls import reverse
from .models import Participant, ScientificWork, Area

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.area = Area.objects.create(name="Test Area")
        self.work = ScientificWork.objects.create(
            title="Test Work",
            authors="Author 1",
            year_of_publication=2023
        )
        self.work.areas.add(self.area)
        self.participant = Participant.objects.create(
            first_name="John",
            last_name="Doe"
        )
        self.participant.works.add(self.work)
    
    def test_create_participant_view(self):
        response = self.client.get(reverse('participant_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'participant_form.html')

    def test_update_participant_view(self):
        response = self.client.get(reverse('participant_update', args=[self.participant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'participant_form.html')

    def test_create_participant_post(self):
        response = self.client.post(reverse('participant_create'), {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'works': [self.work.id]
        })
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Participant.objects.filter(first_name='Jane').exists())


class ModelsTestCase(TestCase):
    def setUp(self):
        self.area = Area.objects.create(name="Test Area")
        self.work = ScientificWork.objects.create(
            title="Unique Test Work",
            authors="Author 1",
            year_of_publication=2023
        )
        self.work.areas.add(self.area)
        self.participant = Participant.objects.create(
            first_name="John",
            last_name="Doe"
        )
        self.participant.works.add(self.work)

    def test_scientific_work_creation(self):
        work = ScientificWork.objects.get(title="Unique Test Work")
        self.assertEqual(work.title, "Unique Test Work")
        self.assertEqual(work.authors, "Author 1")

    def test_participant_creation(self):
        participant = Participant.objects.get(first_name="John")
        self.assertEqual(participant.first_name, "John")
        self.assertEqual(participant.last_name, "Doe")

    def test_add_work_to_participant(self):
        new_work = ScientificWork.objects.create(
            title="Another Test Work",
            authors="Author 2",
            year_of_publication=2024
        )
        self.participant.works.add(new_work)
        self.assertIn(new_work, self.participant.works.all())

class IntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.area = Area.objects.create(name="Test Area")
        self.work = ScientificWork.objects.create(
            title="Integration Test Work",
            authors="Author 1",
            year_of_publication=2023
        )
        self.work.areas.add(self.area)
        self.participant = Participant.objects.create(
            first_name="John",
            last_name="Doe"
        )
        self.participant.works.add(self.work)

    def test_create_participant_and_associate_work(self):
        response = self.client.post(reverse('participant_create'), {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'works': [self.work.id]
        })
        self.assertEqual(response.status_code, 302)
        participant = Participant.objects.get(first_name='Jane')
        self.assertIn(self.work, participant.works.all())
