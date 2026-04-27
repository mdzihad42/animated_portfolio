from django.db import models

class Hero(models.Model):
    title_prefix = models.CharField(max_length=100, default="Providing")
    gradient_text_1 = models.CharField(max_length=100, default="the best")
    title_middle = models.CharField(max_length=100, default="Project")
    gradient_text_2 = models.CharField(max_length=100, default="Experience")
    description = models.TextField()
    hero_video = models.FileField(upload_to='hero/', blank=True, null=True)
    background_video = models.FileField(upload_to='background/', blank=True, null=True)
    
    def __str__(self):
        return "Hero Section Content"

    class Meta:
        verbose_name_plural = "Hero Section"

class About(models.Model):
    title = models.CharField(max_length=200, default="About Me")
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Section"

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

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

    class Meta:
        verbose_name_plural = "Education Section"
        ordering = ['order']

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
