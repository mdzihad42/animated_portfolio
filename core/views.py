from django.shortcuts import render, redirect
from .models import Project, Skill, ContactMessage

def home(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if full_name and email and message:
            ContactMessage.objects.create(full_name=full_name, email=email, message=message)
            return redirect('home')
            
    projects = Project.objects.all().order_by('order')
    skills = Skill.objects.all()
    
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'index.html', context)
