from django.shortcuts import render
from reviews.models import Reviews
from collections import namedtuple

ReviewView = namedtuple('ReviewView', ['reviewText', 'image', 'stars', 'stars_missing'])

def index(request):  
    # Get first three reviews
    dbReviews = Reviews.objects.all()[:3]
    reviews = map(lambda r: ReviewView(reviewText = r.reviewText, image = r.image, stars = range(r.starRating), stars_missing = range(5 - r.starRating)), dbReviews)
    
    return render(request, 'index.html', {'reviews': reviews})
