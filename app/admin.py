from django.contrib import admin
from app.models import *
from django.http import HttpResponse
# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
