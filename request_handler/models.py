from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class items(models.Model):
    item_id = models.TextField(primary_key=True)
    item_description = models.TextField()
    item_state = models.IntegerField()

    class Meta:
        verbose_name_plural = 'items'

    def __str__(self):
        return self.item_description


class loans(models.Model):
    date_on_loan = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    loan_is_finished = models.BooleanField()
    student_id = models.ForeignKey(User, related_name='Loan', on_delete=models.CASCADE)
    item_id = models.ForeignKey(items, related_name='items', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'loans'
