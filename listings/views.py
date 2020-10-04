from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from .models import Listing
from .choices import price_choices, bedroom_choices, state_choices


# Create your views here.
def index(request):
    # this is the way of adding data from python to HTML
    # to fetch data from data base
    # this order by date shows listing by most recent dat and is_published method shows if the current property
    # is un-Checked from the backend, it should not appear at front-end.
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # listings coming from database
    paginator = Paginator(listings, 1)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {

        # now instead of passing listing directly let's pass paged-listings
        # 'listings': listings

        'listings': page_listings
    }
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        "listing": listing
    }
    return render(request, "listings/listing.html", context)


def search(request):
    # this will get all the listings.
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords  # when you are making request through the form you are actually making get request

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        # if keywords is checking you are entering some keyword
        if keywords:
            # description__icontains=keywords this checks the whole paragraph for the typed keyword
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            # description__iexact=city is checking weather exact same city spellings are searched.
            queryset_list = queryset_list.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            # description__iexact=state is checking weather same exact same city spellings are searched.
            queryset_list = queryset_list.filter(state__iexact=state)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            # description__lte= bedroom is checking less than equal to number of bedrooms searched by the user
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        # remember this request.get is going to your form filed and look for this price field.
        price = request.GET['price']
        if price:
            # description__lte= bedroom is checking less than equal to number of bedrooms searched by the user
            queryset_list = queryset_list.filter(price__lte=price)

    context = {

        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        "listings": queryset_list,
        'values': request.GET
    }
    return render(request, "listings/search.html", context)
