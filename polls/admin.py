from django.contrib import admin

# Register your models here.

# tell the admin that Question objects have an admin interface.

from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)