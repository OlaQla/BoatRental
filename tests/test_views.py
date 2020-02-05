from django.test import TestCase
from django.urls import reverse

from boats.models import Boats
import unittest

class BoatsViewsTest(TestCase): 
    @classmethod
    def setUpTestData(cls):
        Boats.objects.create(model = "abc", boatType = "small", price = 110, maxPassangers = 3, cabins = 2, lenght = 10, builtDate = "2010-01-01", image = "test_image.jpg")

    def test_get_all_boats_at_desired_location(self): 
        response = self.client.get('/boats/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_boats_accessible_by_name(self):
        response = self.client.get(reverse('boats'))
        self.assertEqual(response.status_code, 200)

    def test_get_all_boats_has_correct_template(self): 
        response = self.client.get(reverse('boats'))
        self.assertTemplateUsed(response, "boats.html")

    def test_get_boats_details_at_desired_location(self):
        response = self.client.get('/boats/1')
        self.assertEqual(response.status_code, 200)

    @unittest.expectedFailure
    def test_get_boats_details_throws_for_wrong_id(self):
        response = self.client.get('/boats/2')

    def test_get_boat_details_accessible_by_name(self):
        response = self.client.get(reverse('boat_details', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_get_boat_details_has_correct_template(self):
        response = self.client.get(reverse('boat_details', args=(1,)))
        self.assertTemplateUsed(response, "boat_details.html")

        
