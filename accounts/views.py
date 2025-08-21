# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import SignupForm, ProfileForm

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = SignupForm()
    return render(request, 'accounts/register.html', {'form': form})

class SimpleLoginView(LoginView):
    template_name = 'registration/login.html'

class SimpleLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def edit_profile(request):
    profile_form = ProfileForm(instance=request.user)
    pwd_form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if 'save_profile' in request.POST:
            profile_form = ProfileForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('accounts:profile')

        elif 'change_password' in request.POST:
            pwd_form = PasswordChangeForm(user=request.user, data=request.POST)
            if pwd_form.is_valid():
                user = pwd_form.save()
                update_session_auth_hash(request, user)  # no cerrar sesión
                return redirect('accounts:profile')

    return render(request, 'accounts/edit_profile.html', {
        'form': profile_form,
        'pwd_form': pwd_form,
    })
