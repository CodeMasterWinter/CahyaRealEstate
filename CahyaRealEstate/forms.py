from django import forms
from .models import Address, Listing


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['suburb', 'city', 'province']


class ListingForm(AddressForm):
    price_min = forms.IntegerField(required=False, label='Min Price')
    price_max = forms.IntegerField(required=False, label='Max Price')
    rooms = forms.IntegerField(required=False, label='Rooms')
    bathrooms = forms.IntegerField(required=False, label='Bathrooms')

    suburb = forms.CharField(required=False)
    city = forms.CharField(required=False)
    province = forms.CharField(required=False)

    class Meta(AddressForm.Meta):
        fields = AddressForm.Meta.fields + ['price_min', 'price_max', 'rooms', 'bathrooms']