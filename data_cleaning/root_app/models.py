from django.db import models


# Create your models here.
# Model Adress.
class Address(models.Model):
    company = models.CharField(max_length=50, null=False)
    street = models.CharField(max_length=50, null=True)
    Street_number = models.IntegerField(null=True)
    zip = models.IntegerField(null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    byScrapy = models.BooleanField(null=False)
    state = models.CharField(max_length=50, null=True)


class Meta:
    verbose_name = "address"
    ordering = ['zip']


def __str__(self):
    return str(self.way)


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
