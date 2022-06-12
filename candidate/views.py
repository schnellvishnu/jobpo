from django.shortcuts import render ,redirect

# Create your views here.
from django.views.generic import TemplateView,CreateView,FormView,ListView
from candidate.forms import Candidateprofileform,Candidateprofileupdateform
from candidate.models import Candidateprofile
from django.urls import reverse_lazy
from employer.models import User,Jobs
class Candidatehomeview(TemplateView):
    template_name = "candidate/cand-home.html"

class Candidateprofileview(CreateView):
    model = Candidateprofile
    form_class = Candidateprofileform
    template_name = "candidate/cand-profile.html"
    success_url = reverse_lazy("cand-home")


    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class CandidateprofileDetailview(TemplateView):
    template_name = "candidate/cand-profiledetail.html"


class CandidateUpdateprofileview(FormView):
    template_name = "candidate/cand-editprofile.html"
    form_class = Candidateprofileupdateform
    def get(self,request,*args,**kwargs):
        profile_details=Candidateprofile.objects.get(user=request.user)
        form=Candidateprofileupdateform(instance=profile_details,initial={"first_name":request.user.first_name,"last_name":request.user.last_name,"phone":request.user.phone,"eamil":request.user.email})
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        profiledetails=Candidateprofile.objects.get(user=request.user)
        form=self.form_class(instance=profiledetails,data=request.POST,files=request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data.pop("first_name")
            last_name=form.cleaned_data.pop("last_name")
            phone=form.cleaned_data.pop("phone")
            email=form.cleaned_data.pop("email")
            user=User.objects.get(id=request.user.id)
            user.first_name=first_name
            user.last_name=last_name
            user.phone=phone
            user.email=email
            user.save()
            return redirect("cand-home")
        else:
            return render(request.template_name,{"form":form})


class Candidatejoblistview(ListView):
    model=Jobs
    context_object_name = "jobs"
    template_name = "candidate/joblist.html"
    def get_queryset(self):
        return self.model.objects.all().order_by("-created_date")

