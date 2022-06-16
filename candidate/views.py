from django.shortcuts import render ,redirect

# Create your views here.
from django.views.generic import TemplateView,CreateView,FormView,ListView,DetailView
from candidate.forms import Candidateprofileform,Candidateprofileupdateform
from candidate.models import Candidateprofile
from django.urls import reverse_lazy
from employer.models import User,Jobs,Application
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages


class Candidatehomeview(TemplateView):
    template_name = "candidate/cand-home.html"

def signout_view(request, *args, **kwargs):
        logout(request)
        return redirect("signin")


class Changepasswordview(TemplateView):
    template_name = "candidate/changepassword.html"

    def post(self, request, *args, **kwargs):
        pwd = request.POST.get("pwd")
        uname = request.user
        user = authenticate(request, username=uname, password=pwd)
        if user:
            return redirect("password-reset")

        else:
            return render(request, self.template_name)


class Passwordresetview(TemplateView):
    template_name = "candidate/passwordreset.html"

    def post(self, request, *args, **kwargs):
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        if pwd1 != pwd2:
            return render(request, self.template_name, {"mag": "incorrect password"})
        else:
            u = User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect("signin")


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

class Candidatejobdetailview(DetailView):
    model = Jobs
    context_object_name = "job"
    template_name = "candidate/job-details.html"
    pk_url_kwarg = "id"


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        is_applied=Application.objects.filter(applicant=self.request.user,job=self.object)
        print(is_applied)
        context["is_applied"]=is_applied
        return context

def apply_now(request, *args, **kwargs):
    user=request.user
    job_id=kwargs.get("id")
    job = Jobs.objects.get(id=job_id)
    Application.objects.create(applicant=user,
                               job=job
                               )
    messages.success(request, "your application has posted successfully")
    return redirect("cand-home")






class ApplicationListview(ListView):
    model = Application
    template_name = "candidate/cand-applications.html"
    context_object_name = "applications"
    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user).exclude(status="cancelled")



def cancell_application(request,*args,**kwargs):
    app_id=kwargs.get("id")
    application=Application.objects.get(id=app_id)
    application.status="cancelled"
    application.save()
    messages.success(request,"your application cancelled")
    return redirect("cand-home")
