from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from newspaper.forms import NewspaperForm, RedactorCreationForm, RedactorUpdateForm, NewspaperSearchForm, \
    RedactorSearchForm
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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = RedactorSearchForm(initial={"username": username})
        return context

    def get_queryset(self):
        form = RedactorSearchForm(self.request.GET)
        queryset = super().get_queryset()

        if form.is_valid():
            username = form.cleaned_data.get("username")
            if username:
                queryset = queryset.filter(username__icontains=username)
        return queryset


class RedactorDetailView(DetailView):
    model = Redactor


class RedactorCreateView(LoginRequiredMixin, CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newspaper:index")


class RedactorUpdateView(LoginRequiredMixin, UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    success_url = reverse_lazy("newspaper:redactors")


class RedactorDeleteView(LoginRequiredMixin, DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactors")


class TopicListView(ListView):
    model = Topic
    paginate_by = 10


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topics")


class NewspaperListView(ListView):
    model = Newspaper
    paginate_by = 5
    queryset = Newspaper.objects.prefetch_related("topics").prefetch_related("publishers")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = NewspaperSearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        form = NewspaperSearchForm(self.request.GET)
        queryset = super().get_queryset()

        if form.is_valid():
            title = form.cleaned_data.get("title")
            if title:
                queryset = queryset.filter(title__icontains=title)
        return queryset


class NewspaperDetailView(DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspapers")


class NewspaperDeleteView(LoginRequiredMixin, DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspapers")


class NewspaperUpdateView(LoginRequiredMixin, UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspapers")
