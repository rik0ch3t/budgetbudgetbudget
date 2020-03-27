from django.contrib.auth.models import User, Group
from budget.models import Budget, Expense, Category
from rest_framework import serializers


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['uuid', 'name', 'category', 'budgeted', 'available', 'spent', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    expenses = ExpenseSerializer(many=True)

    class Meta:
        model = Category
        fields = ['uuid', 'name', 'budget', 'expenses', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        expense_data = validated_data.pop('expenses')
        category = Category.object.create(**validated_data)
        for expense in expense_data:
            Expense.objects.create(category=category, **expense_data)
        return category

    def update(self, instance, validated_data):
        # update basic category fields, if update info exists
        instance.name = validated_data.get('name', instance.name)
        instance.budget = validated_data.get('budget', instance.budget)
        instance.save()

        # create mappings for easy id-to-obj references
        expenses_mapping = {expense.uuid: expense for expense in instance.expenses}
        data_mapping = {data['uuid']: data for data in validated_data.get('expenses')}

        # update expenses, create new ones if necessary
        for uuid, data in data_mapping.items():
            expense_data = expenses_mapping.get(uuid, None)
            if expense_data is None:
                Expense.objects.create(category=instance, **expense_data)
            else:
                expense.name = expense_data['name']
                expense.budgeted = expense_data['budgeted']
                expense.available = expense_data['available']
                expense.spent = expense_data['spent']
                expense.save()

        return instance


class BudgetSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Budget
        fields = ['uuid', 'name', 'categories', 'capital', 'strategy', 'created_at', 'updated_at']

    def create(self, validated_data):
        category_data = validated_data.pop('categories')
        budget = Budget.object.create(**validated_data)
        for category in category_data:
            Category.objects.create(budget=budget, **category_data)
        return budget

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.capital = validated_data.get('capital', instance.capital)
        instance.strategy = validated_data.get('strategy', instance.strategy)
        instance.save()

        categories_mapping = {category.uuid: category for category in instance.categories}
        data_mapping = {data['uuid']: data for data in validated_data.get('categories')}

        for uuid, data in data_mapping.items():
            category_data = categories_mapping.get(uuid, None)
            if category_data is None:
                Category.objects.create(budget=instance, **category_data)
            else:
                category.name = category_data['name']
                category.budgeted = category_data['budgeted']
                category.available = category_data['available']
                category.spent = category_data['spent']
                category.save()

        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
