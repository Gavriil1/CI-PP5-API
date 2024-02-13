from rest_framework import generics, permissions
from djangoapi.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticated]  # Changed to IsAuthenticated
    serializer_class = LikeSerializer

    def get_queryset(self):  # Added get_queryset method
        return Like.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(owner=self.request.user)
