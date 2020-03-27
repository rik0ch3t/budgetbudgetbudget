from django.db import models

import uuid

ZERO_BASED = "ZB"
FIFTY_THIRTY_TWENTY = "FTT"
STRATEGIES = [(ZERO_BASED, "zero-based"), (FIFTY_THIRTY_TWENTY,"50/30/20")]


class Budget(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True)
    name = models.CharField(max_length=80, default='')
    capital = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    strategy = models.CharField(choices=STRATEGIES, default=ZERO_BASED, max_length=3)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        ordering = ['created_at']

    def change_name(self):
        pass

    def add_capital(self):
        pass

    def remove_capital(self):
        pass

    def new_category(self):
        pass

    def change_strategy(self):
        pass
        ''
    def move_expense_capital(self):
        pass

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True)
    name = models.CharField(max_length=80, default='')
    budget = models.ForeignKey(Budget, related_name='categories', on_delete=models.CASCADE, default='', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        ordering = ['created_at']

    def change_name(self):
        pass

    def new_expense(self):
        pass

    def __str__(self):
        return f"{self.name}"

class Expense(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True)
    name = models.CharField(max_length=80, default='')
    category = models.ForeignKey(Category, related_name='expenses', on_delete=models.CASCADE, default='', blank=True, null=True)
    budgeted = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    available = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    spent = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        ordering = ['created_at']

    def change_name(self):
        pass

    def ajdust_available_amount(self):
        pass

    def adjust_spent_amount(self):
        pass

    def adjust_budgeted_amount(self):
        pass

    def __str__(self):
        return f"{self.name}"