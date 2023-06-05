from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.models import Group


# Extend the default user model 
class UserProfile(models.Model):
    role_choices = (
        ('Doctor', 'Doctor'), 
        ('Nurse', 'Nurse'), 
        ('Pharm', 'Pharm'), 
        ('Desk', 'Desk')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=role_choices)

    # Override the save method (to add users to groups when created)
    def save(self, *args, **kwargs):
        get_group = Group.objects.get(name=self.role_choices)
        get_group.user_set.add(self.user)
        get_group.save()
        super(UserProfile, self).save(*args, **kwargs)
