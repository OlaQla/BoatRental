from django.shortcuts import render
from reviews.models import Reviews
from boats.models import FeaturedBoat, Boats
from collections import namedtuple

# View of a Review for rendering purposes to avoid having logic in templates
ReviewView = namedtuple(
    'ReviewView', [
        'reviewText', 'image', 'stars', 'stars_missing'])

# Render main / welcome page
def index(request):
    # Get first three reviews
    dbReviews = Reviews.objects.all()[:3]

    # map reviews from database object to view objects
    reviews = map(
        lambda r: ReviewView(
            reviewText=r.reviewText, image=r.image, stars=range(
                r.starRating), stars_missing=range(
                5 - r.starRating)), dbReviews)

    # Load featured boats from database
    featuredBoats = map(lambda fb: fb.boat, FeaturedBoat.objects.all()[:3])

    # Pass loaded data to index template
    return render(
        request, 'index.html', {
            'reviews': reviews, 'featured_boats': featuredBoats})
