from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Contact
from .serializers import ContactSerializer

# Viewset for managing contacts.
class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'company']


    def get_queryset(self):
        # Return contacts for the authenticated user.
        return Contact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user to the authenticated user.
        serializer.save(user=self.request.user)
