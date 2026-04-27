from django.shortcuts import render, redirect
from .models import Hero, About, Skill, Education, Project, ContactMessage

def home(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if full_name and email and message:
            ContactMessage.objects.create(full_name=full_name, email=email, message=message)
            return redirect('home')
            
    hero = Hero.objects.first()
    about = About.objects.first()
    skills = Skill.objects.all()
    educations = Education.objects.all().order_by('order')
    projects = Project.objects.all().order_by('order')
    
    context = {
        'hero': hero,
        'about': about,
        'skills': skills,
        'educations': educations,
        'projects': projects,
    }
    return render(request, 'index.html', context)
