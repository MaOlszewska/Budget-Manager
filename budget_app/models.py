from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExpenseInformation(models.Model):
    CATEGORY_CHOICES = (
        ('Zakupy', 'Zakupy'),
        ('Kosmetyki', 'Kosmetyki'),
        ('Odzież', 'Odzież'),
        ('Transport', 'Transport'),
        ('Rozrywka', 'Rozrywka'),
        ('Edukacja', 'Edukacja'),
        ('Zdrowie', 'Zdrowie'),
        ('Inne', 'Inne'),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=11, choices=CATEGORY_CHOICES, default='Inne')
    description = models.TextField(null = True, blank = True)
    expense = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description
