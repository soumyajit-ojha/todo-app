from django.db import models


class Status(models.TextChoices):
        PENDING     = "pending"
        IN_PROGRESS = 'in_progress'
        DONE        = "done"
        CANCELED    = "canceled"


class Todo(models.Model):
    title       = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    target_date = models.DateTimeField(null=True, blank=True)
    completed   = models.BooleanField(default=False)
    status      = models.CharField(
          max_length=15,
          choices=Status.choices,
          default=Status.PENDING
    )

    def __str__(self):
          return f"{self.title}"
    
    class Meta:
        app_label = 'todo'
        verbose_name_plural  = 'todo'
        db_table = 'todo'