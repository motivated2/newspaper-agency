from django.urls import path

from newspaper.views import index, RedactorListView, TopicListView, NewspaperListView, NewspaperCreateView, \
    TopicCreateView

urlpatterns = [
    path('', index, name='index'),
    path('redactors/', RedactorListView.as_view(), name='redactors'),
    path('topics/', TopicListView.as_view(), name='topics'),
    path('topics/create/', TopicCreateView.as_view(), name='topic-create'),
    path('newspapers/', NewspaperListView.as_view(), name='newspapers'),
    path('newspapers/create/', NewspaperCreateView.as_view(), name='newspaper-create'),
]
app_name = 'newspaper'
