from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,ListView,CreateView,DetailView,FormView,UpdateView
# Create your views here.
from employer.models import Jobs,Companyprofile
# from django.contrib.auth.models import User
from employer.models import User,Application
from employer.forms import Signupform,Loginform,Passwordresetform,Companyprofileform
from django.contrib.auth import authenticate,login,logout
#List,Detail,Update,Delete,
from employer.forms import JobForm
from django.urls import reverse_lazy
class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"


class AddJobView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-addjob.html"
    success_url = reverse_lazy("all-jobs")
    # def get(self,request):
    #     form=JobForm()
    #     return render(request,"emp-addjob.html",{"form":form})
    # def post(self,request):
    #     form=JobForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,"emp-home.html")
    #     else:
    #         return render(request,"emp-addjob.html",{"form":form})
    def form_valid(self, form):
        form.instance.company=self.request.user
        return super().form_valid(form)
class Listjobview(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-listjob.html"
    # def get(self,request):
    #     qs=Jobs.objects.all()
    #     return render(request,"emp-listjob.html",{"jobs":qs})
    def get_queryset(self):
        return Jobs.objects.filter(company=self.request.user)


class Jobdetailview(DetailView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-detailsjob.html"
    pk_url_kwarg = "id"
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     return render(request,"emp-detailsjob.html",{"job":qs})





class Jobeditview(View):
    def get(self,request,id):
        qs=Jobs.objects.get(id=id)
        form=JobForm(instance=qs)
        return render(request,"emp-editjob.html",{"form":form})

    def post(self,request,id):
        qs=Jobs.objects.get(id=id)
        form=JobForm(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            return redirect("all-jobs")
        else:
            return render(request,"emp-addjob.html",{"form":form})





class Jobdeleteview(View):
    def get(self,request,id):
        qs=Jobs.objects.get(id=id)
        qs.delete()
        return redirect("all-jobs")


class Signupform(CreateView):
    model=User
    form_class = Signupform
    template_name = "usersignup.html"
    success_url = reverse_lazy("signin")


class Signinview(FormView):
    form_class = Loginform
    template_name = "login.html"

    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                if request.user.role=="employer":
                    return redirect("all-jobs")
                elif request.user.role=="candidate":
                    # return render(request,"candidate/cand-home.html")
                    return redirect("cand-home")


            else:
                return render(request,"login.html",{"form":form})


def signout_view(request,*args,**kwargs):
        logout(request)
        return redirect("signin")



class Changepasswordview(TemplateView):
    template_name = "changepassword.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect("password-reset")
        

        else:
            return render(request,self.template_name)



class Passwordresetview(TemplateView):
    template_name = "passwordreset.html"
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get('pwd1')
        pwd2=request.POST.get('pwd2')
        if pwd1!=pwd2:
            return render(request,self.template_name,{"mag":"incorrect password"})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect("signin")





class Companyprofileview(CreateView):
    model=Companyprofile
    form_class = Companyprofileform
    template_name = "emp-addprofile.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class Empviewprofileview(TemplateView):
    template_name = "emp-profile.html"







class Empprofileeditview(UpdateView):
    model = Companyprofile
    form_class = Companyprofileform
    template_name = "emp-editprofile.html"
    success_url = reverse_lazy("emp-profile")
    pk_url_kwarg = "id"
#
class EmployerApplicationList(ListView):
    model=Application
    context_object_name = "applications"
    template_name = "emp-applicationlist.html"
    def get_queryset(self):
        return Application.objects.filter(job=self.kwargs.get("id")) .exclude(status="cancelled")


class EmployerApplicationDetailview(DetailView):
    model = Application
    context_object_name = "application"
    template_name = "emp-appdetail.html"
    pk_url_kwarg = "id"