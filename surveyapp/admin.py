from lib2to3.pgen2.token import OP
from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import *

admin.site.register(Questions)
admin.site.register(Options)
admin.site.register(Answers)

# LogEntry.objects.all().delete()
