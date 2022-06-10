from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,CreateView
from candidate.forms import Candidateprofileform
from candidate.models import Candidateprofile
from django.urls import reverse_lazy
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