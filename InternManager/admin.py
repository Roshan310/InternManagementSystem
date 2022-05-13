from asyncio import Task
from django.contrib import admin
from .models import Task, Intern, SuperVisor, Assign, Attendence

# Register your models here.
admin.site.register(Task)
admin.site.register(Intern)
admin.site.register(SuperVisor)
admin.site.register(Assign)
admin.site.register(Attendence)
