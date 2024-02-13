# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.utils import timezone
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# model describe database of contact form
class Contact(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name
