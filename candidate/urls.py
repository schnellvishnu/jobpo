from candidate import views

from django.urls import path

urlpatterns=[
    path("home",views.Candidatehomeview.as_view(),name="cand-home"),
    path("profile/add",views.Candidateprofileview.as_view(),name="cand-profile")
]