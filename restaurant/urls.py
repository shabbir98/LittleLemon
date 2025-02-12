# define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"tables", views.BookingViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.MenuItemsView.as_view(), name="menu-items"),
    path(
        "menu/<int:pk>",
        views.SingleMenuItemView.as_view(),
    ),
    path("booking/", include(router.urls)),
]
