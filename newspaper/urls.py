from django.urls import path

from newspaper.views import index, RedactorListView, TopicListView, NewspaperListView

urlpatterns = [
    path('', index, name='index'),
    path('redactors/', RedactorListView.as_view(), name='redactors'),
    path('topics/', TopicListView.as_view(), name='topics'),
    path('newspapers/', NewspaperListView.as_view(), name='newspapers'),
]
app_name = 'newspaper'
