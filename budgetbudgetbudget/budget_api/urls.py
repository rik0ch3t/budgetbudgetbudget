from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from budget_api import views

urlpatterns = [
    path('api/v1/budget', views.BudgetList.as_view()),
    path('api/v1/budget/<uuid:pk>/', views.BudgetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)