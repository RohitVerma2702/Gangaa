from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_amount = models.IntegerField(null=True, blank=True)
#     payment_method = models.CharField(max_length=255, choices=METHODS, default='Cash')
#     payment_status = models.CharField(max_length=255, choices=PAYMENTSTATUS, default='Due')
#     items = models.ManyToManyField(OrderItems, blank=True)
#     order_status = models.CharField(max_length=50, choices=ORDERSTATUS, default='Processing')

#     # def __str__(self):
#     #     return self.id

#     class Meta:
#         verbose_name_plural = "Orders"

#     def date_good(self):
#         return self.date.strftime('%b %e %Y')