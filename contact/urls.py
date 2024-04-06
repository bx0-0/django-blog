from django.urls import path
from .views import ContactView, SuccessContact

app_name = 'contact'

urlpatterns = [
    path('',ContactView.as_view(),name='contact-us'),
    path('success/',SuccessContact.as_view(),name='contact_success'),
]