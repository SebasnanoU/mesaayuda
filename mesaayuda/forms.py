from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = '__all__'
        labels = {
            'name': 'name',
            'email': 'email',
            'subject': 'subject',
            'message': 'message',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
    