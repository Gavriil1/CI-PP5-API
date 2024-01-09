# # Imports
# # Third Party
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# # Internal:
# from rest_framework import generics
# from .models import Contact
# from .serializers import ContactSerializer

# # @login_required
# lass ContactCreateView(generics.CreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer


# contactform/views.py
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer