from django.shortcuts import render
from django.views import generic
from Buchungssystem.models import *
# Create your views here.


class Calender(generic.DetailView):
    model = Appointment
    template_name = 'appointment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
