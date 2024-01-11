from rest_framework import serializers
from notes.models import Notes

class NotesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Notes  # Corrected model name
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'created_at', 'updated_at',
            'title', 'content',
        ]
