from email.policy import default
from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import BooleanField 
# Create your models here.
class User(AbstractUser):
    @property
    def is_intern(self):
        if hasattr(self, 'intern'):
            return True
        return False
    @property
    def is_SuperVisor(self):
        if hasattr(self, 'SuperVisor'):
            return True
        return False
class Intern(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SuperVisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    content = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content

class Assign(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(SuperVisor, on_delete=models.CASCADE)

class Attendence(models.Model):
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default='False')

    def __str__(self):
        intern_name = Intern.objects.get(name=self.intern)
        return intern_name.name