from django.test import TestCase
from django.urls import reverse

from boats.models import Boats
import unittest

# Test views in boats application
class BoatsViewsTest(TestCase):

    # Static method creating test object in a database
    @classmethod
    def setUpTestData(cls):
        Boats.objects.create(
            model="abc",
            boatType="small",
            price=110,
            maxPassangers=3,
            cabins=2,
            lenght=10,
            builtDate="2010-01-01",
            image="test_image.jpg")

    # Check if getting all boats is successful
    def test_get_all_boats_at_desired_location(self):
        response = self.client.get('/boats/')
        self.assertEqual(response.status_code, 200)

    # Check if get all boats page can be referenced by name
    def test_get_all_boats_accessible_by_name(self):
        response = self.client.get(reverse('boats'))
        self.assertEqual(response.status_code, 200)

    # Check if boats.html template is rendered by view getting all boats
    def test_get_all_boats_has_correct_template(self):
        response = self.client.get(reverse('boats'))
        self.assertTemplateUsed(response, "boats.html")

    # Check if boat details view is successful
    def test_get_boats_details_at_desired_location(self):
        response = self.client.get('/boats/1')
        self.assertEqual(response.status_code, 200)

    # Check confirming failure when non existing boat is tried to be loaded
    @unittest.expectedFailure
    def test_get_boats_details_throws_for_wrong_id(self):
        response = self.client.get('/boats/2')

    # Check if boat details page can be referenced by name
    def test_get_boat_details_accessible_by_name(self):
        response = self.client.get(reverse('boat_details', args=(1,)))
        self.assertEqual(response.status_code, 200)

    # Check if boat details view is using correct template
    def test_get_boat_details_has_correct_template(self):
        response = self.client.get(reverse('boat_details', args=(1,)))
        self.assertTemplateUsed(response, "boat_details.html")
