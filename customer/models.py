from django.db import models

# Create your models here.

class Customer_info(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    static_addr = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name