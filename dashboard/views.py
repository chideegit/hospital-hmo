from django.shortcuts import render, redirect

def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)