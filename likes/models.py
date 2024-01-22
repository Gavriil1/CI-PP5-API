from django.db import models
from django.contrib.auth.models import User
from notes.models import Notes



class Like(models.Model):
    """
    Like model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    notelike = models.ForeignKey(
        Notes, related_name='notelike', on_delete=models.CASCADE, default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # unique_together = ['owner', 'notelike']

    def __str__(self):
        return f'{self.owner} {self.notelike}'