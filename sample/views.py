from django.shortcuts import render


def index(request):
    context = {
        "title": "Django-tailwindcss",
        "button_body": "click me !"
    }
    return render(request, "index.html", context)