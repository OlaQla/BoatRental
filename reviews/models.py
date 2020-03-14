from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Reviews(models.Model):
    reviewText = models.CharField(max_length=254, default='')
    starRating = models.IntegerField(default=5,
                                     validators=[
                                         MaxValueValidator(5),
                                         MinValueValidator(1)
                                     ])
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.reviewText
