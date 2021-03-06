from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path("", login_required(views.IndexView.as_view()), name="menu-index"),
    path("<uuid:uuid>/", views.menu_link, name="menu-link"),
    path(
        "<uuid:uuid>/add/option/<int:option_id>/",
        views.menu_select_option,
        name="menu-select-option",
    ),
    path(
        "<uuid:uuid>/delete/option/<int:employee_option_id>/",
        views.menu_delete_option,
        name="menu-delete-option",
    ),
    path("<int:pk>/", login_required(views.DetailView.as_view()), name="menu-detail"),
    path("create/", login_required(views.MenuCreateView.as_view()), name="menu-create"),
    path("<int:pk>/update/", login_required(views.menu_update), name="menu-update"),
    # path('<int:pk>/update/', views.MenuUpdateView.as_view(), name='menu-update'),
]
