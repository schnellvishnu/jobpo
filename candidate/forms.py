from django import forms
from candidate.models import Candidateprofile
class Candidateprofileform(forms.ModelForm):
    class Meta:
        model=Candidateprofile
        exclude=("user",)
        widgets={
            "profile_pic":forms.FileInput(attrs={"class":"form-control rounded-pill"}),
            "qualification":forms.TextInput(attrs={"class":"form-control rounded-pill"}),
            "skills":forms.TextInput(attrs={"class":"form-control rounded-pill"}),
            "resume":forms.FileInput(attrs={"class":"form-control rounded-pill"}),
            "experience":forms.NumberInput(attrs={"class":"form-control rounded-pill"}),
            "location":forms.TextInput(attrs={"class":"form-control rounded-pill"}),
            "age": forms.NumberInput(attrs={"class": "form-control rounded-pill"}),

        }
class Candidateprofileupdateform(forms.ModelForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    phone=forms.CharField()
    email=forms.CharField(max_length=120)
    class Meta:
        model=Candidateprofile
        fields=["first_name",
                "last_name",
                "phone",
                "email",
                "profile_pic",
                "resume",
                "location",
                "age",
                "skills",
                "qualification"]
