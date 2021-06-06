from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='menu-index'),
    path('<int:pk>/', login_required(views.DetailView.as_view()), name='menu-detail'),
    path('create/', login_required(views.create), name='menu-create'),
    path('<int:pk>/update/', views.MenuUpdateView.as_view(), name='menu-update'),
]