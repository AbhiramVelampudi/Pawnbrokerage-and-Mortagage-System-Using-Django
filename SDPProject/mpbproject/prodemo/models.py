from django.db import models

# Create your models here.
class Registration(models.Model):
    email = models.EmailField(max_length=50, blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    registrationtime=models.DateTimeField(blank=False,auto_now=True)

    class Meta:
        db_table = "registration_table"