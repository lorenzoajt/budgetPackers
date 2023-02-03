from django.contrib import admin
from .models import Trip, Expense

# Register your models here.
admin.site.register(Trip)


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'created_at', 'type_of_expense', 'trip')
    pass
admin.site.register(Expense, ExpenseAdmin)