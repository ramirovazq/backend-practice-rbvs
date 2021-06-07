from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path(
        "create/menu/<int:menu_pk>/", login_required(views.create), name="option-create"
    ),
    path(
        "<int:pk>/",
        login_required(views.OptionDetailView.as_view()),
        name="option-detail",
    ),
    path(
        "menu/<int:menu_pk>/update/<int:pk>/",
        login_required(views.OptionUpdateView.as_view()),
        name="option-update",
    ),
    path(
        "menu/<int:menu_pk>/delete/<int:pk>/",
        login_required(views.OptionDeleteView.as_view()),
        name="option-delete",
    ),
]
