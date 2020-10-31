from django.db import models

# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=200)
    experience = models.TextField()
    image = models.ImageField(blank=True)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    degree = models.CharField(max_length=200)
    college = models.CharField(max_length=400)
    university = models.CharField(max_length=400)
    email = models.EmailField(max_length=200)
    website = models.URLField(max_length=200,default=None)

    def __str__(self):
        return self.name 
    


class Project(models.Model):
    title = models.CharField(max_length=200)
    sub_discription = models.CharField(max_length=30)
    discription = models.TextField()
    language = models.CharField(max_length=200)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200)
    github = models.URLField(max_length=200)
    website = models.URLField(max_length=200, default=None)
    Resume = models.ForeignKey(Resume, related_name="projects",null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']