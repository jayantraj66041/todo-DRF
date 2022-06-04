from django.contrib import admin
from api.models import TodoModel
# Register your models here.

# Register TodoModel on the admin panel to show on dashboard.
admin.site.register(TodoModel)