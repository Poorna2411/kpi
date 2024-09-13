from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CaptchaLoginForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .forms import KPIForm
from .models import KPI



def home(request):                              #home page
    template = loader.get_template("inde.html")
    return HttpResponse(template.render())

def login(request):                              #login page
    if request.method == 'POST':
        form = CaptchaLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Use the built-in login function
                return redirect('user_details')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid CAPTCHA')
    else:
        form = CaptchaLoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def user_details(request):
    profile = request.user.profile  # Access the user's profile
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_details')  # After saving, redirect to the same page
    else:
        form = ProfileUpdateForm(instance=profile)
    
    context = {
        'user': request.user,
        'form': form,
    }
    
    return render(request, 'user_details.html', context)

@login_required
def add_kpi(request):
    if request.method == 'POST':
        form = KPIForm(request.POST)
        if form.is_valid():
            kpi = form.save(commit=False)
            kpi.user = request.user  # Save KPI under the logged-in user
            kpi.save()
            messages.success(request, 'KPI added successfully!')
            return redirect('add_kpi')
    else:
        form = KPIForm()

    # Only show the KPIs created by the logged-in user
    previous_kpis = KPI.objects.filter(user=request.user)
    return render(request, 'add_kpi.html', {'form': form, 'previous_kpis': previous_kpis})

@login_required
def delete_kpi(request, kpi_id):
    kpi = get_object_or_404(KPI, id=kpi_id, user=request.user)  # Ensure user can only delete their own KPIs
    if request.method == 'POST':
        kpi.delete()
        messages.success(request, 'KPI deleted successfully!')
    return redirect('add_kpi')