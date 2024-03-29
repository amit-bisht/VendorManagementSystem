from django.db import models

class Vendor(models.Model):
    name=models.CharField(max_length=10)
    contact_details=models.TextField()
    address=models.TextField()
    vendor_code=models.CharField(unique=True,max_length=20)
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()

    def __str__(self):
        return self.name

