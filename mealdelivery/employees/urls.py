from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.EmployeesIndexView.as_view()), name='employees-index'),
    path('<int:pk>/', login_required(views.EmployeeDetailView.as_view()), name='employee-detail'),
    path('create/', login_required(views.EmployeeCreateView.as_view()), name='employee-create'),
    path('<int:pk>/update/', login_required(views.EmployeeUpdateView.as_view()), name='employee-update'),
    path('<int:pk>/delete/', login_required(views.EmployeeDeleteView.as_view()), name='employee-delete'),
]