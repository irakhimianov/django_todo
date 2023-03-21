from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect

User = get_user_model()


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('task_list')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        authenticated_user = authenticate(username=username, password=password)
        login(self.request, authenticated_user)
        return redirect(self.success_url)


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('task_list')
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = 'login'
