from django.contrib import admin
from employer import views
from django.urls import path
urlpatterns = [
path("home",views.EmployerHomeView.as_view(),name="emp-home"),
    path("jobs/add",views.AddJobView.as_view(),name="emp-addjob"),
    path('jobs/all',views.Listjobview.as_view(),name="all-jobs"),
    path('jobs/details/<int:id>',views.Jobdetailview.as_view(),name='jobdetail'),
    path("jobs/change/<int:id>",views.Jobeditview.as_view(),name="emp-editjob"),
    path("jobs/delete/<int:id>",views.Jobdeleteview.as_view(),name="emp-deletejob"),
    path("users/account/signup",views.Signupform.as_view(),name="signup"),
    path("users/accounts/signin",views.Signinview.as_view(),name="signin"),
    path("users/accounts/signout",views.signout_view,name="signout"),
    path("users/password/change",views.Changepasswordview.as_view(),name="password-change"),
    path("users/password/reset",views.Passwordresetview.as_view(),name="password-reset"),
    path("profile/add",views.Companyprofileview.as_view(),name="emp-addprofile"),
    path("profile/detail",views.Empviewprofileview.as_view(),name="emp-profile"),
    path("profile/edit/<int:id>",views.Empprofileeditview.as_view(),name="emp-editprofile")

]

