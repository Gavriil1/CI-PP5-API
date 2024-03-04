# Imports
# External:
from django.contrib import admin
# Internal:
from .models import Contact

# registration of Contact Form to admin panel
admin.site.register(Contact)
