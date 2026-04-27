from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('designer', 'Designer'),
        ('coder', 'Coder'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='skills/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.full_name}"
