from django.test import TestCase
from .models import Boats

class BoatsTests(TestCase):
    """
    tests that we'll run against Boat model
    """

    def test_str(self):
        test_model = Boats(model='ABC')
        self.assertEqual(str(test_model), 'ABC')
