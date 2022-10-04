from django.urls import path
from . import views

app_name = 'mesaayuda'
urlpatterns = [
    path('', views.TicketsView.as_view(), name='tickets'),
    path('ticket_create/', views.TicketCreateView.as_view(), name='ticket_create'),
    path('ticket/<int:pk>/', views.TicketDetailView.as_view(), name='ticket-detail'),
    path('ticket/<int:pk>/update/', views.TicketUpdateView.as_view(), name='ticket-update'),
    path('ticket/<int:pk>/delete/', views.TicketDeleteView.as_view(), name='ticket-delete'),
]
