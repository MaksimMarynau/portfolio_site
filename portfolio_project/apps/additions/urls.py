from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("about/", views.about_view, name="about_view"),
    path("about/tools/", views.tools_view, name="tools_view"),
    path("about/tools/<int:id>", views.tool_detail, name="tool_detail"),
    path("work/", views.work_view, name="work_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("success/", views.success_view, name="success"),


]
