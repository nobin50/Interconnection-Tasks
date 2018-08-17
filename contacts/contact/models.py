from django.db import models

class Contact_List(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    district = models.CharField(max_length=60)

    def __str__(self):
        return self.name