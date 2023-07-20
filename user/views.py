from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.views.generic import View

from user.forms import UserCreationForm


class RegisterView(View):
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return resolve_url(self.request.GET.get('next', 'home'))

class CustomLoginView(LoginView):
    def get_success_url(self):
        # The template has a parameter that gets the page the user is currently on that is called "next"
        # so that way a user is not redirected to the home page.
        return resolve_url(self.request.GET.get('next', 'home'))

class CustomLogoutView(LogoutView):
    def get_next_page(self):
        return resolve_url(self.request.GET.get('next', 'home'))