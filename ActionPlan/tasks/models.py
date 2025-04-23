from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Task(models.Model): 
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('school', 'School'),
        ('other', 'Other'),
    ]

    COMPLETION_CHOICES = [
        ('not completed', 'Not Completed'),
        ('completed', 'Completed'),
    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    completed = models.CharField(max_length=20, choices=COMPLETION_CHOICES, default='not completed')
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.completed == 'completed' and self.completed_at is None:
            self.completed_at = timezone.now()
        elif self.completed != 'completed':
            self.completed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.description}, {self.priority}, {self.category}, {self.completed})"


