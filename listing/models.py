from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import pre_save

from real_state.utils import get_generate_slug

User = get_user_model()


class Listing(models.Model):
    class SaleType(models.Choices):
        RENT = 'rent'
        SALE = 'sale'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='listing/%Y,%m,%d', blank=True, null=True)
    sale_type = models.CharField(max_length=40, choices=SaleType.choices, default=SaleType.RENT)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    bed_room = models.IntegerField(blank=True, null=True)
    bath_room = models.IntegerField(blank=True, null=True)
    square_feet = models.IntegerField()

    # address
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.PositiveIntegerField(blank=True, null=True)

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Listing)
def listing_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = get_generate_slug(instance)
