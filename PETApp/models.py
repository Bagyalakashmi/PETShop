from django.db import models
from django.utils import timezone


# Create your models here.
class PetModel(models.Model):
    Id = models.BigAutoField(primary_key=True)
    owner = models.CharField(max_length=256, null=False, default="")
    petName = models.CharField(max_length=256, blank=False, null=False)
    petImage = models.ImageField(upload_to='images', null=False, blank=False)
    type = models.CharField(max_length=256, null=False, blank=False,default="non")
    category = models.CharField(max_length=256, blank=False, null=False,default="non")
    amount = models.IntegerField(default="0")
    Created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.petName
