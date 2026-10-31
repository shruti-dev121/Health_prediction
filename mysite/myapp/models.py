from django.db import models

# Create your models here.
from django.db import models

class Details(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email_address = models.EmailField(unique=True)
    glucose = models.FloatField()
    haemoglobin = models.FloatField()
    cholesterol = models.FloatField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name