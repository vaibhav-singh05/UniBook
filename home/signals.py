from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a Profile when a new User is created
        Profile.objects.create(user=instance, profile_pic='profile_pics/default.jpg')
    else:
        # Save the Profile when the User is updated
        instance.profile.save()
