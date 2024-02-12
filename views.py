from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Link
from .forms import LinkForm


# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {"links": links}
    return render(request, "links/index.html", context)


# shortened url -> original url (destination)
def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()

    return redirect(link.url)


def add_link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            # save the data and return the user to home page
            form.save()
            return redirect(reverse("home"))
    else:
        form = LinkForm()
    context = {
        "form": form,
    }

    return render(request, "links/create.html", context)
