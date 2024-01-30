from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from djangoapi.permissions import IsOwnerOrReadOnly
from .models import Notes  # Fix import
from .serializers import NotesSerializer  # Fix import

class NotesList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = NotesSerializer  # Fix serializer class
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    # filterset_fields = [
    #     'owner__followed__owner__profile',
    #     'likes__owner__profile',
    #     'owner__profile',
    # ]
    # search_fields = [
    #     'owner__username',
    #     'title',
    # ]

    filterset_fields = [
        # 'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    # ordering_fields = [
    #     'likes__created_at',
    # ]



    def get_queryset(self):
        # return Notes.objects.all()
        return Notes.objects.filter(owner=self.request.user)
        # return Note.objects.filter(owner=user)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = NotesSerializer  # Fix serializer class
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Notes.objects.filter(owner=self.request.user)