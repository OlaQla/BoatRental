import datetime

import django
from django.test import TestCase
from django.utils import timezone

from checkout import forms

# Tests covering checkout forms
class TestMakePaymentForm(TestCase):

    # Check if credit_card_number field has correct label
    def test_credit_card_number_field_label(self):
        form = forms.MakePaymentForm()
        self.assertTrue(
            form.fields['credit_card_number'].label == "Credit card number")

    # Check if credit_card_number field is not required as it is validated by Stripe, not in Django backend
    def test_credit_card_number_field_required(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['credit_card_number'].required == False)

    # Check if cvv field has correct label
    def test_cvv_field_label(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['cvv'].label == "Security code (CVV)")

    # Check if cvv field is not requires as it is validated by String, not in Django backend
    def test_cvv_field_required(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['cvv'].required == False)

    # Check if expiry_month field has a correct label
    def test_expiry_month_field_label(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['expiry_month'].label == "Month")

    # Check if expiry_month field is not required as it is validated by stripe, not in Django backend
    def test_expiry_month_field_required(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['expiry_month'].required == False)

    # Check if expiry_month field has 12 choices representing months in a year
    def test_expiry_month_field_choices(self):
        form = forms.MakePaymentForm()
        choices = form.fields["expiry_month"].choices

        for i in range(12):
            self.assertEqual(choices[i], (i + 1, i + 1))

    # Check if expiry_year field has correct label
    def test_expiry_year_field__label(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['expiry_year'].label == "Year")

    # Check if expiry_year field is not requiredm because they are validated by stripe not django backend
    def test_expiry_year_field_required(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['expiry_year'].required == False)

    # Check if expiry_year field has 10 consecutive year choices starting 2020
    def test_expiry_year_field_choices(self):
        form = forms.MakePaymentForm()
        choices = form.fields["expiry_year"].choices

        for i in range(10):
            self.assertEqual(choices[i], (2020 + i, 2020 + i))

    # Check if stripe_id is not visuble to users
    def test_stripe_id_field_is_hidden(self):
        form = forms.MakePaymentForm()
        self.assertEqual(
            type(
                form.fields["stripe_id"].widget),
            django.forms.HiddenInput)
