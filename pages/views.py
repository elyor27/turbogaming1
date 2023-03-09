from django.views.generic import TemplateView, CreateView
from pages.forms import ContactModelForm
from django.urls import reverse
# from django.contrib.auth.mixins import LoginRequiredMixin


class HomeTemplateViews(TemplateView):
    template_name = 'index.html'


class ContactCreateViews(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')
