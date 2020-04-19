from django.db import models

# Create your models here.

class Store(models.Model):
    district = models.CharField(max_length=250, null=True, blank=True)
    block = models.CharField(max_length=250, null=True, blank=True)
    gram_panchayat = models.CharField(max_length=250, null=True, blank=True)
    village = models.CharField(max_length=250, null=True, blank=True)
    store_type = models.CharField(max_length=250, null=True, blank=True)
    store_name = models.CharField(max_length=250, null=True, blank=True)
    owner_name = models.CharField(max_length=250, null=True, blank=True)
    contact_number = models.CharField(max_length=250, null=True, blank=True)
    pincode = models.CharField(max_length=250, null=True, blank=True)
    products = models.CharField(max_length=250, null=True, blank=True)
    delivery_area = models.CharField(max_length=250, null=True, blank=True)
    delivery_status = models.CharField(max_length=250, null=True, blank=True)
    remark = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name_plural = "Stores"