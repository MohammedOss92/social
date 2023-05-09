from django.urls import path ,include
from landing.views import Index

urlpatterns = [
    path('',Index.as_view(),name='index'),
     
    path('accounts/', include('allauth.urls')),
]