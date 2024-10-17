from django.urls import path
from . import views


urlpatterns = [
    path('jobsIO/', views.get_landing_page, name='get-landing-page'),
]