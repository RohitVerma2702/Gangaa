from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    shop_id = models.CharField(max_length=50)
    shop_name = models.CharField(max_length=50, null=True, blank=True)
    shop_type = models.CharField(max_length=50, null=True, blank=True)
    merchant = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    doe = models.DateTimeField(null=True, blank=True)
    gstin = models.CharField(max_length=50, null=True, blank=True)
    gstcert = models.ImageField(upload_to='emp-docs/cv/', blank=True, null=True)
    idproof = models.ImageField(upload_to='emp-docs/idproof/', blank=True, null=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    location_lat = models.DecimalField(max_digits=20, decimal_places=6)
    location_lon = models.DecimalField(max_digits=20, decimal_places=6)

    def __str__(self):
        return self.shop_id

    class Meta:
        verbose_name_plural = "Shops"

    def date_good(self):
        return self.doe.strftime('%b %e %Y')