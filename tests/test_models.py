from django.test import TestCase
from boats.models import Boats

# Tests covering boats model types and constraints
class BoatModelTest(TestCase):

    # Static method setting up test data in database
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
            image="")

    # Check if model field has correct name
    def test_model_name(self):
        boat = Boats.objects.get(id=1)
        field_label = boat._meta.get_field("model").verbose_name
        self.assertEquals(field_label, "model")

    # Check boat type field has correct name
    def test_boat_type_name(self):
        boat = Boats.objects.get(id=1)
        field_label = boat._meta.get_field("boatType").verbose_name
        self.assertEquals(field_label, "boatType")
    
    # Check if max passangers field has two digits capacity
    def test_max_passangers_max_digits(self):
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("maxPassangers")
        self.assertEquals(field.max_digits, 2)

    # Check max passangers does not have decimal places (is integer)
    def test_max_passangers_decimal_places(self):
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("maxPassangers")
        self.assertEquals(field.decimal_places, 0)

    # Check cabins field has two digits capacity
    def test_cabins_max_digits(self):
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("cabins")
        self.assertEquals(field.max_digits, 2)

    # Check cabins fiels does not have decimal places (is integer)
    def test_cabins_decimal_places(self):
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("cabins")
        self.assertEquals(field.decimal_places, 0)

    # Check if length field has six digits capacity
    def test_length_max_digits(self):
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("lenght")
        self.assertEquals(field.max_digits, 6)

    # Check if length field has two decimal places (is a floating point number)
    def test_length_decimal_places(self):
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("lenght")
        self.assertEquals(field.decimal_places, 2)

    # Check if build date field has correct name
    def test_built_date_field(self):
        boat = Boats.objects.get(id=1)
        field_label = boat._meta.get_field("builtDate").verbose_name
        self.assertEquals(field_label, "builtDate")

    # Check if image field has correct name
    def test_image_field(self):
        boat = Boats.objects.get(id=1)
        field_label = boat._meta.get_field("image").verbose_name
        self.assertEquals(field_label, "image")
