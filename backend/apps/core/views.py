from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm


def home(request):
    return render(request, "home.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                subject=f"Readex contact message from {name}",
                message=message,
                from_email=email,
                recipient_list=["admin@readex.local"],
            )

            messages.success(
                request,
                "Your message has been sent successfully!",
            )

            form = ContactForm()

    else:
        form = ContactForm()

    return render(
        request,
        "contact.html",
        {"form": form},
    )