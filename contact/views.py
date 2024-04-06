from typing import Any
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

# Create your views here.


class ContactView(LoginRequiredMixin, FormView):
    form_class = ContactForm
    template_name = "contact/contact.html"
    success_url = "success/"

    def form_valid(self, form: Any) -> HttpResponse:
        title = form.cleaned_data.get("title")
        message_content = form.cleaned_data.get("message_content")
        first_name = form.cleaned_data.get("first_name")
        user_name = form.cleaned_data.get("user_name")
        message_content += f" from {first_name}-{user_name}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [form.cleaned_data.get("email")]
        send_mail(title, message_content, email_from, recipient_list)

        return super().form_valid(form)

class SuccessContact(LoginRequiredMixin, TemplateView):
    template_name = "contact/success.html"
