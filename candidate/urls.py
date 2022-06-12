from candidate import views

from django.urls import path

urlpatterns=[
    path("home",views.Candidatehomeview.as_view(),name="cand-home"),
    path("profile/add",views.Candidateprofileview.as_view(),name="cand-profile"),
    path("profile/detail",views.CandidateprofileDetailview.as_view(),name="cand-profiledetail"),
    path("profile/change",views.CandidateUpdateprofileview.as_view(),name="cand-profileEDIT"),
    path("jobs/all",views.Candidatejoblistview.as_view(),name="cand-joblist")
]