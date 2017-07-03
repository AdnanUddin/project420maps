from django.contrib import admin
from django.conf.urls import url

from .models import Question

admin.site.register(Question)

# Register your models here.

