from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    options=(
        ("employer","employer"),
        ("candidate","candidate")
    )
    role=models.CharField(max_length=120,choices=options,default="candidate")
    phone=models.CharField(max_length=12,null=True)
    location=models.CharField(max_length=120)
    email=models.CharField(max_length=120)









class Jobs(models.Model):
    job_title_name = models.CharField(max_length=150)
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company")
    location = models.CharField(max_length=120)
    salary = models.PositiveIntegerField(null=True)
    experience = models.PositiveIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    last_date = models.DateField(null=True)
    active_status = models.BooleanField(default=True)


def __init__(self):
    return self.job_title


class Companyprofile(models.Model):
    company_name = models.CharField(max_length=120)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employer")
    location = models.CharField(max_length=120)
    services = models.CharField(max_length=120)
    logo = models.ImageField(upload_to="companyprofile", null=True)
