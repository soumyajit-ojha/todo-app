from django.db import models
from user.models import CustomUser


class Status(models.TextChoices):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    CANCELED = "canceled"


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    target_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True
    )
    status = models.CharField(
        max_length=15, choices=Status.choices, default=Status.PENDING
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        app_label = "todo"
        verbose_name_plural = "todo"
        db_table = "todo"
