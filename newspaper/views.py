from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from newspaper.forms import NewspaperForm
from newspaper.models import Redactor, Topic, Newspaper


def index(request):
    """View function for the home page of the site."""

    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    num_newspapers = Newspaper.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_newspapers": num_newspapers,
        "num_visits": num_visits + 1,
    }

    return render(request, "newspaper/index.html", context=context)


class RedactorListView(ListView):
    model = Redactor


class TopicListView(ListView):
    model = Topic


class TopicCreateView(CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topics")


class NewspaperListView(ListView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspapers")
