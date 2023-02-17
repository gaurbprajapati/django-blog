# from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed

from django.db.models.signals import post_save

from django.contrib.auth.models import User

from django.dispatch import receiver

from .models import Profile


# if new object is insert or created the create==true
# instance==is the new user that is created
# sender==django.contrib.auth.models.user

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs) -> None:

    # when the new user is create than created is true and it create/add the profile for the new user
    if created:
        Profile.objects.create(user=instance)


'''
    # @receiver(post_save, sender=User)
    # or
    # post_save.connect(create_profile,sender=User)
'''


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs) -> None:
    instance.profile.save()
