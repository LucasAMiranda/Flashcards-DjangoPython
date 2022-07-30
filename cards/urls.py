from django.urls import path
from django.views.generic import TemplateView 

from cards.views import CardCreateView, CardListView, CardUpdateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="cards/base.html")),
    path('list/', CardListView.as_view(), name="card-list"),
    path('new/', CardCreateView.as_view(), name="card-create"),
    path('edit/<int:pk>', CardUpdateView.as_view(), name="card-update")
]