from django.shortcuts import render, redirect
from django.views import generic

from .models import Ticket
from .forms import TicketForm


class TicketsView(generic.ListView):        
    template_name = 'ticket/tickets.html'
    context_object_name = "tickets"
    
    def get_queryset(self):
        return Ticket.objects.all()
    


class TicketCreateView(generic.CreateView):
    model = Ticket
    template_name = 'ticket/ticket_create.html'
    form_class = TicketForm
    success_url = '/mesaayuda'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TicketDetailView(generic.DetailView):
    model = Ticket
    template_name = 'ticket/ticket-detail.html'
    context_object_name = "ticket"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class TicketUpdateView(generic.UpdateView):
    model = Ticket
    template_name = 'ticket/ticket-update.html'
    form_class = TicketForm
    success_url = '/mesaayuda'


class TicketDeleteView(generic.DeleteView):
    model = Ticket
    template_name = 'ticket/ticket-delete.html'
    form_class = TicketForm
    success_url = '/mesaayuda'