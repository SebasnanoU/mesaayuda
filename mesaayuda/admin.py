from pyexpat import model
from django.contrib import admin

from .models import Ticket

admin.site.register(Ticket)
models = Ticket
