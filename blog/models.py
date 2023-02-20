from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)

    # deneder/magic/special method :- str method user to show the data in

    def __str__(self) -> str:
        return self.title

# this is will find the location for specific post detail
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})
