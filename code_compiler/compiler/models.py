from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CodeSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    language = models.CharField(max_length=20, choices=[('python', 'Python'), ('java', 'Java'), ('c', 'C')])
    code = models.TextField()
    output = models.TextField(blank=True,null=True)
    error_message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class ErrorLog(models.Model):
    submission = models.OneToOneField(CodeSubmission, on_delete=models.CASCADE)
    ai_suggestion = models.TextField()