from django.contrib import messages
from django.shortcuts import render, redirect

from django.core.mail import send_mail#

# Create your views here.
from .models import Contact


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if users has already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for thid listing")
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, message=message, phone=phone,
                          user_id=user_id)

        contact.save()
        """
      # send email
        send_mail(
            'Property Listing Inquiry',
            "There has been inquiry for " + listing + ". Sign into admin panel for more information.",


        )
"""
        messages.success(request, "Your request has been submitted, a realtor will get back to you soon")
        return redirect('/listings/' + listing_id)
