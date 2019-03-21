from django.db import models
from django.utils.timezone import now


class Product(models.Model):
    GENDER_CHOICES = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )
    code = models.TextField(max_length=255, null=False, blank=False, default=0)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default='M'
    )
    colour = models.TextField(max_length=255, null=False, blank=False, default='')
    size = models.IntegerField(null=False, blank=False, default=0)
    created_on = models.DateTimeField(default=now)
    date_of_sale = models.DateTimeField(null=True, blank=True)
