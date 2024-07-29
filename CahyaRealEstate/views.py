import os
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Address, Listing
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.core.files.uploadedfile import SimpleUploadedFile


def home(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = request.POST['full_name']
            sender_name = request.POST['full_name']
            sender_company = request.POST['company']
            sender_email = request.POST['email']
            sender_phone = request.POST['phone']
            sender_message = request.POST['message']
            sender_service = request.POST['service']
            sender_property = request.POST['property']

            try:

                sender_message = f"Email Address: {sender_email}\nPhone: {sender_phone}\n\nMessage:\n{sender_message}"
                send_mail(
                    f'''{sender_name} from {sender_company} wants to {sender_service} their {sender_property}''',
                    sender_message,
                    sender_email,
                    ['rhulanimogotsi@gmail.com', 'rhulanimogotsi28@gmail.com']
                )

                messages.success(request, 'We got your Message! One of our agents will reach out soon!')
                return redirect('home')
            except BadHeaderError:
                return HttpResponse('Invalid Header')
    else:
        form = ContactForm()

    context = {
        'page_title': "Home",
        "contactform": form
    }

    return render(request, 'CahyaRealEstate/home.html', context)

def populate_properties(request):

    properties = [
        {
            "street": "123 Main St", "suburb": "Sandton", "city": "Johannesburg", "province": "Gauteng",
            "price": 1500000, "description": "Modern apartment with a view", "rooms": 2, "image_path": "1.jpg",
            "bathrooms": 1
        },
        {
            "street": "456 Elm St", "suburb": "Sea Point", "city": "Cape Town", "province": "Western Cape",
            "price": 3000000, "description": "Luxury beachfront villa", "rooms": 4, "image_path": "2.jpg",
            "bathrooms": 3
        },
        {
            "street": "789 Oak St", "suburb": "Umhlanga Rocks", "city": "Durban", "province": "KwaZulu-Natal",
            "price": 2500000, "description": "Spacious family home", "rooms": 3, "image_path": "3.jpg",
            "bathrooms": 2
        },
        {
            "street": "101 Pine St", "suburb": "Stellenbosch Central", "city": "Stellenbosch",
            "province": "Western Cape",
            "price": 1800000, "description": "Cosy cottage in wine country", "rooms": 2, "image_path": "4.jpg",
            "bathrooms": 1
        },
        {
            "street": "234 Maple St", "suburb": "Constantia", "city": "Cape Town", "province": "Western Cape",
            "price": 3500000, "description": "Elegant mansion with a pool", "rooms": 5, "image_path": "5.jpg",
            "bathrooms": 4
        },
        {
            "street": "567 Birch St", "suburb": "Bryanston", "city": "Johannesburg", "province": "Gauteng",
            "price": 2800000, "description": "Executive residence with garden", "rooms": 4,
            "image_path": "6.jpg", "bathrooms": 3
        },
        {
            "street": "890 Cedar St", "suburb": "Knysna Central", "city": "Knysna", "province": "Western Cape",
            "price": 2200000, "description": "Seaside retreat with panoramic views", "rooms": 3,
            "image_path": "7.jpg", "bathrooms": 2
        },
        {
            "street": "111 Pineapple St", "suburb": "Hout Bay", "city": "Cape Town", "province": "Western Cape",
            "price": 3200000, "description": "Cliffside villa overlooking the bay", "rooms": 4,
            "image_path": "8.jpg", "bathrooms": 3
        },
        {
            "street": "222 Watermelon St", "suburb": "Paarl Central", "city": "Paarl", "province": "Western Cape",
            "price": 2000000, "description": "Historic manor amidst vineyards", "rooms": 4,
            "image_path": "9.jpg", "bathrooms": 3
        },
        {
            "street": "333 Banana St", "suburb": "Plettenberg Bay Central", "city": "Plettenberg Bay",
            "province": "Western Cape",
            "price": 2900000, "description": "Luxury beach house with private access", "rooms": 3,
            "image_path": "10.jpg", "bathrooms": 2
        },
        {
            "street": "444 Avocado St", "suburb": "Fourways Gardens", "city": "Johannesburg", "province": "Gauteng",
            "price": 2600000, "description": "Exclusive estate living", "rooms": 5, "image_path": "11.jpg",
            "bathrooms": 4
        },
        {
            "street": "555 Guava St", "suburb": "Waterkloof Ridge", "city": "Pretoria", "province": "Gauteng",
            "price": 3400000, "description": "Architectural masterpiece", "rooms": 6, "image_path": "12.jpg",
            "bathrooms": 5
        }
    ]

    for prop in properties:
        address = Address.objects.create(
            street=prop["street"],
            suburb=prop["suburb"],
            city=prop["city"],
            province=prop["province"]
        )

        # Construct the full path to the image file (relative to static directory)
        image_path = os.path.join('C:\\', 'CahyaRealEstate', 'CahyaRealEstate', 'static', 'CahyaRealEstate', 'images', 'properties', prop["image_path"])

        # Open the image file
        with open(image_path, 'rb') as img_file:

            img_data = img_file.read()
            image = SimpleUploadedFile(prop["image_path"], img_data, content_type='image/jpeg')

            # Create the Listing object with the image file
            listing = Listing.objects.create(
                price=prop["price"],
                description=prop["description"],
                rooms=prop["rooms"],
                image=image,
                bathrooms=prop["bathrooms"],
                address=address
            )

    return render(request, 'CahyaRealEstate/index.html', {'message': 'Properties populated successfully.'})