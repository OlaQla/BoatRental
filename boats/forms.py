from django import forms

"""
    Form for searching boats
"""
class BoatSearchForm(forms.Form):
    search_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search term'}),
        required=False)
    min_cabins = forms.IntegerField(
        label="",
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Min cabins'}),
        required=False)
    min_passangers = forms.IntegerField(
        label="",
        min_value=1,
        max_value=50,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Min guests'}),
        required=False)
    include_sailboat = forms.BooleanField(label="", required=False)
    include_powerboat = forms.BooleanField(label="", required=False)
    include_catamaran = forms.BooleanField(label="", required=False)
    include_motoryacht = forms.BooleanField(label="", required=False)
