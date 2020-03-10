from django.db import models
from boats.models import Boats
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Comment(models.Model):
    commentText = models.CharField(max_length=254, default='')
    date = models.DateField(auto_now=True)
    boat = models.ForeignKey(Boats)
    user = models.ForeignKey(User)
    starRating = models.IntegerField(default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    
    def __str__(self):
        return f'{self.user.username}-{self.boat.model}-{self.starRating}-{self.date}'