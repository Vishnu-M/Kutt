from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(UserURL)
admin.site.register(AnonymousURL)
admin.site.register(UserPhoneNumber)
admin.site.register(UserURLStatistics)