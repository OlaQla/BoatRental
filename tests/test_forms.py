import datetime

import django
from django.test import TestCase
from django.utils import timezone

from checkout import forms

class TestMakePaymentForm(TestCase): 
    
    def test_credit_card_number_field_label(self): 
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['credit_card_number'].label == "Credit card number")
    
    def test_credit_card_number_field_required(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['credit_card_number'].required == False)

    def test_cvv_field_label(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['cvv'].label == "Security code (CVV)")

    def test_cvv_field_required(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['cvv'].required == False)

    def test_expiry_month_field_label(self): 
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['expiry_month'].label == "Month")
    
    def test_expiry_month_field_required(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['expiry_month'].required == False)

    def test_expiry_month_field_choices(self):
        form = forms.MakePaymentForm()
        choices = form.fields["expiry_month"].choices
        
        for i in range(12):
            self.assertEqual(choices[i], (i + 1, i + 1))

    def test_expiry_year_field__label(self): 
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['expiry_year'].label == "Year")
    
    def test_expiry_year_field_required(self):
        form = forms.MakePaymentForm()
        self.assertTrue(form.fields['expiry_year'].required == False)

    def test_expiry_year_field_choices(self):
        form = forms.MakePaymentForm()
        choices = form.fields["expiry_year"].choices

        for i in range(11): 
            self.assertEqual(choices[i], (2020 + i, 2020 + i))

    def test_stripe_id_field_is_hidden(self):
        form = forms.MakePaymentForm()
        self.assertEqual(type(form.fields["stripe_id"].widget), django.forms.HiddenInput)

