from django.db import models


# Skill model to represent individual skills
class Skill(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


# Experience model to represent work experiences
class Experience(models.Model):
    company_name = models.CharField(max_length=200)
    company_url = models.URLField(max_length=300, null=True, blank=True)
    position = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skill, related_name='experiences')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company_name}"



# Portfolio model to represent portfolio items
class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    description = models.TextField()
    project_url = models.URLField(max_length=300, null=True, blank=True)
    tech_skills = models.ManyToManyField(Skill, related_name='portfolio_items')
    is_future = models.BooleanField(default=False)
    github_url = models.URLField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


# Message model to represent messages sent via contact form
class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
