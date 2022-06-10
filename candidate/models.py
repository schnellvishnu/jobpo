from django.db import models

# Create your models here.
from employer.models import User
class Candidateprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="candidate")
    profile_pic=models.ImageField(upload_to="candidate")
    resume=models.FileField(upload_to="cv",null=True)
    qualification=models.CharField(max_length=120)
    skills=models.CharField(max_length=120)
    experience=models.PositiveIntegerField(default=0)
    age=models.PositiveIntegerField(default=0)
    location=models.CharField(max_length=120)



