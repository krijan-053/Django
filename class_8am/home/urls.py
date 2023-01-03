from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryViews.as_view(), name='category'),
    path('brand/<slug>', BrandViews.as_view(), name='brand'),
    path('detail/<slug>', ProductDetailView.as_view(), name='detail'),

]