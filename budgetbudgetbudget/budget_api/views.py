# django
from django.contrib.auth.models import User, Group
from django.http import Http404

# rest framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics

# local
from budget.models import Budget, Category, Expense
from budget_api.serializers import UserSerializer, GroupSerializer, BudgetSerializer, CategorySerializer, ExpenseSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BudgetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows budgets to be viewed or edited.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetList(generics.ListCreateAPIView):
    """
    List all code budgets, or create a new budget.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a budget.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer