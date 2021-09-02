from django.urls import path
from . import views

urlpatterns = [
    path("", views.portofolio_index, name='index'),
    path("<int:pk>/", views.portofolio_detail, name='detail'),
]