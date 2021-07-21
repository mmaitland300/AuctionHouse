from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, AuctionListing, Bid, Comment, Watchlist


def index(request):
    active_listings = AuctionListing.objects.all().filter(active=True)
    bids = Bid.objects.all()
    return render(request, "auctions/index.html", {
        "listings": active_listings,
        "bids": bids,
        "message": "Active Listings"
    })


def closed_listings(request):
    closed_listings = AuctionListing.objects.all().filter(active=False)
    bids = Bid.objects.all()
    return render(request, "auctions/index.html", {
        "listings": closed_listings,
        "bids": bids,
        "message": "Inactive Listings"
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect('index')
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            title = request.POST['title']
            description = request.POST['description']
            category = request.POST['category']
            start_bid = request.POST['start_bid']
            image = request.POST['image']
            new_listing = AuctionListing.objects.create(
                                user = user,
                                title = title,
                                description = description,
                                category = category,
                                start_bid = start_bid,
                                image = image
                                )
            new_listing.save()
            return redirect('index')
        else:
            return render(request, "auctions/create.html", {
                "error": "Log in to create a listing."
            })
    
    return render(request, "auctions/create.html")


def listing(request, listing_id):
    user = request.user
    listing = AuctionListing.objects.filter(id=listing_id).first()
    bids = Bid.objects.filter(listing=listing)
    comments = Comment.objects.filter(listing=listing).order_by('-post_time')
    high_bid = listing.start_bid

    if bids:
        for bid in bids:
            if bid.value > high_bid:
                high_bid = bid.value

    if request.method == 'POST':
        user = request.user
        value = request.POST.get('bid', None)
        comment = request.POST.get('comment', None)
        
        if value:
            if int(value) < high_bid:
                return redirect('listing', listing_id)
            new_bid = Bid.objects.create(
                user = user,
                value = int(value),
                listing = listing
            )
            new_bid.save()
            old_bid = Bid.objects.filter(listing=listing).exclude(value=value)
            old_bid.delete()
            return redirect('listing', listing_id)

        if comment:
            new_comment = Comment.objects.create(
                user = user,
                listing = listing,
                content = comment
            )
            return redirect('listing', listing_id)

    if request.user.is_authenticated:
        watchlist = Watchlist.objects.filter(user=user, listing=listing)
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "watchlist": watchlist,
            "comments": comments,
            "high_bid": high_bid,
            "min_bid": (high_bid + 1)
        })
    
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "comments": comments,
            "high_bid": high_bid,
            "min_bid": (high_bid + 1)
        })


def close(request, listing_id):
    user = request.user
    listing = AuctionListing.objects.filter(id=listing_id).first()
    bid = Bid.objects.filter(listing=listing).first()
    if listing.user == user and bid is not None:
        listing.active = False
        listing.winner = bid.user
        listing.save()
        return redirect("index")
    elif listing.user == user and bid is None:
        listing.active = False
        listing.delete()
        return redirect("index")


def add_item(request, listing_id):
    user = request.user
    item = AuctionListing.objects.filter(id=listing_id).first()
    watchlist = Watchlist.objects.filter(user=user, listing=item)
    if not watchlist:
        add_item = Watchlist.objects.create(user=user, listing=item)
        add_item.save()
        return redirect("listing", listing_id)


def remove_item(request, listing_id):
    user = request.user
    item = AuctionListing.objects.filter(id=listing_id).first()
    watchlist = Watchlist.objects.filter(user=user, listing=item)
    if watchlist:
        watchlist.delete()
        return redirect("listing", listing_id)


def watchlist(request):
    user = request.user
    wlist = Watchlist.objects.filter(user=user)
    return render(request, "auctions/watchlist.html", {
        "items": wlist
    })

def categories(request):
    categories = AuctionListing.objects.values_list('category', flat=True).distinct()
    return render(request, "auctions/category.html", {
        "categories": categories
    })

def category_listings(request, category):
    listings = AuctionListing.objects.filter(category=category)
    return render(request, "auctions/category_listings.html", {
        "listings": listings,
        "category": category,
    })



