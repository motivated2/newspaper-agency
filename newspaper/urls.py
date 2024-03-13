from django.urls import path

from newspaper.views import (
    index,
    RedactorListView,
    TopicListView,
    NewspaperListView,
    NewspaperCreateView,
    TopicCreateView,
    RedactorDetailView,
    NewspaperDetailView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    NewspaperDeleteView,
    NewspaperUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactors"),
    path("redactors/create", RedactorCreateView.as_view(), name="redactor-create"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path(
        "redactors/<int:pk>/update",
        RedactorUpdateView.as_view(),
        name="redactor-update",
    ),
    path(
        "redactors/<int:pk>/delete",
        RedactorDeleteView.as_view(),
        name="redactor-delete",
    ),
    path("topics/", TopicListView.as_view(), name="topics"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("newspapers/", NewspaperListView.as_view(), name="newspapers"),
    path("newspapers/<int:pk>", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path(
        "newspapers/<int:pk>/delete",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
    path(
        "newspapers/<int:pk>/update",
        NewspaperUpdateView.as_view(),
        name="newspaper-update",
    ),
]
app_name = "newspaper"
