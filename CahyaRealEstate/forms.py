from django import forms
from .models import Address, Listing


services = [('sell', 'I want to SELL...'),
            ('buy', 'I want to BUY...'),
            ('rent_out', "Rent out (I'm an owner)"),
            ('rent_in', 'I want to rent...'),
            ]

properties = [('apartment', 'an Apartment'),
              ('house', 'a House'),
              ('land', 'Land'),
              ('commercial', 'a Commercial Property'),
              ]


class ContactForm(forms.Form):

    full_name = forms.CharField(required=True)
    company = forms.CharField(required=False, label="Company Name (Optional)")
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    service = forms.ChoiceField(required=True, choices=services)
    property = forms.ChoiceField(required=True, choices=properties)
    message = forms.CharField(widget=forms.Textarea, required=True)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['suburb', 'city', 'province']


class ListingForm(AddressForm):
    price_min = forms.IntegerField(required=False, label='Min Price')
    price_max = forms.IntegerField(required=False, label='Max Price')
    rooms = forms.IntegerField(required=False, label='Rooms')
    bathrooms = forms.IntegerField(required=False, label='Bathrooms')
    location_search = forms.CharField(required=False, label='Location Search')

    suburb = forms.CharField(required=False)
    city = forms.CharField(required=False)
    province = forms.CharField(required=False)

    class Meta(AddressForm.Meta):
        fields = AddressForm.Meta.fields + ['price_min', 'price_max', 'rooms', 'bathrooms', 'location_search']