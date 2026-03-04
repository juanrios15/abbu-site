from django.shortcuts import render
from .models import HomePage, ServicesPage, AboutPage, Quote


def home(request):
    page = HomePage.get_solo()
    quote = Quote.objects.order_by("?").first()
    return render(request, "sitecontent/home.html", {"page": page, "quote": quote})


def services(request):
    page = ServicesPage.get_solo()
    return render(request, "sitecontent/services.html", {"page": page})


def about(request):
    page = AboutPage.get_solo()
    return render(request, "sitecontent/about.html", {"page": page})


def contact(request):
    return render(request, "sitecontent/contact.html")