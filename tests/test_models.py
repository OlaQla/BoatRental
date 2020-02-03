from django.test import TestCase
from boats.models import Boats

class BoatModelTest(TestCase): 
    @classmethod
    def setUpTestData(cls):
        Boats.objects.create(model = "abc", boatType = "small", price = 110, maxPassangers = 3, cabins = 2, lenght = 10, builtDate = "2010-01-01", image = "")

    def test_model_name(self): 
        boat = Boats.objects.get(id=1)
        field_label = boat._meta.get_field("model").verbose_name
        self.assertEquals(field_label, "model")

    def test_boat_type_name(self): 
        boat = Boats.objects.get(id=1)
        field_label = boat._meta.get_field("boatType").verbose_name
        self.assertEquals(field_label, "boatType")

    def test_max_passangers_max_digits(self): 
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("maxPassangers")
        self.assertEquals(field.max_digits, 2)

    def test_max_passangers_decimal_places(self): 
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("maxPassangers")
        self.assertEquals(field.decimal_places, 0)

    def test_cabins_max_digits(self): 
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("cabins")
        self.assertEquals(field.max_digits, 2)

    def test_cabins_decimal_places(self): 
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("cabins")
        self.assertEquals(field.decimal_places, 0)
    
    def test_length_max_digits(self): 
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("lenght")
        self.assertEquals(field.max_digits, 6)

    def test_length_decimal_places(self): 
        boat = Boats.objects.get(id=1)
        field = boat._meta.get_field("lenght")
        self.assertEquals(field.decimal_places, 2)

    def test_built_date_field(self): 
        boat = Boats.objects.get(id=1)
        field_label = boat._meta.get_field("builtDate").verbose_name
        self.assertEquals(field_label, "builtDate")

    def test_image_field(self): 
        boat = Boats.objects.get(id=1)
        field_label = boat._meta.get_field("image").verbose_name
        self.assertEquals(field_label, "image")
