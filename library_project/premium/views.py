from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Premium

@login_required
def upgrade_premium(request):
    return render(request, 'upgrade_premium.html')


@login_required
def activate_premium(request):
    Premium.objects.get_or_create(user=request.user)
    messages.success(request, "Premium activated")
    return redirect('home')


@login_required
def premium_members(request):
    members = Premium.objects.select_related('user')
    return render(request, 'premium_members.html', {'members': members})
