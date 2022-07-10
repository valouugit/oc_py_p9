from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    healine = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.ticket.title


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following"
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_user",
    )

    def __str__(self) -> str:
        return f"{self.followed_user} follow {self.user}"
    
    class Meta:
        unique_together = ('user', 'followed_user', )
