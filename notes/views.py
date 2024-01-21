from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from djangoapi.permissions import IsOwnerOrReadOnly
from .models import Notes
from .serializers import NotesSerializer

class NotesList(generics.ListCreateAPIView):
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]

    def get_queryset(self):
        # Return only notes associated with the currently authenticated user
        if self.request.user.is_authenticated:
            return Notes.objects.filter(owner=self.request.user)
        return Notes.objects.none()  # If not authenticated, return an empty queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotesSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        # Return only the note owned by the currently authenticated user
        if self.request.user.is_authenticated:
            return Notes.objects.filter(owner=self.request.user)
        return Notes.objects.none()  # If not authenticated, return an empty queryset
