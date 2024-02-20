from candidate import views

from django.urls import path

urlpatterns=[
    path("home",views.Candidatehomeview.as_view(),name="cand-home"),
    path("profile/add",views.Candidateprofileview.as_view(),name="cand-profile"),
    path("profile/detail",views.CandidateprofileDetailview.as_view(),name="cand-profiledetail"),
    path("profile/change",views.CandidateUpdateprofileview.as_view(),name="cand-profileEDIT"),
    path("jobs/all",views.Candidatejoblistview.as_view(),name="cand-joblist"),
    path("users/password/change", views.Changepasswordview.as_view(), name="password-change"),
    path("users/password/reset", views.Passwordresetview.as_view(), name="password-reset"),
    path("users/accounts/signout", views.signout_view, name="signout"),
    path("jobs/details/<int:id>",views.Candidatejobdetailview.as_view(),name="cand-jobdetails"),
    path("jobs/apply-now/<int:id>",views.apply_now,name="applynow"),
    path("applications/all",views.ApplicationListview.as_view(),name="cand-application"),
    path("applications/remove/<int:id>",views.cancell_application,name="cand-cancelapplication")

]