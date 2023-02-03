from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns

# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    budget_limit = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""        
        return reverse('trip-detail', args=[str(self.id)])

class Expense(models.Model):    
    GENERAL = 'GR'
    TRAVEL = 'TR'
    FOOD = 'FD'
    ACCOMODATION = 'AC'    
    EXPENSE_CHOICES = [
        (GENERAL, 'General'),
        (TRAVEL, 'Travel'),
        (FOOD, 'Food'),
        (ACCOMODATION, 'Accomodation'),        
    ]
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    type_of_expense = models.CharField(max_length=2, choices=EXPENSE_CHOICES, default=GENERAL,)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""        
        return reverse('expense-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

    