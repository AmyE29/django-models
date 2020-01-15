from django.urls import path
from .views import HomePageView, FlavorDetailView


urlpatterns = [
    path('', HomePageView.as_view() , name = 'home'),
    path('icecream/<int:pk>/', FlavorDetailView.as_view(), name='flavors_details')
]
