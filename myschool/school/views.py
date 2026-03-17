from django.shortcuts import render
from .models import Student

# Create your views here.

def index(request):
    return render(request, "index.html")

def cms(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname", "").strip()
        lastname = request.POST.get("lastname", "").strip()
        age = request.POST.get("age", "").strip()
        gender = request.POST.get("gender", "").strip()

        student = Student.objects.create(
            firstname = firstname,
            lastname = lastname,
            age = int(age) if age else 0,
            gender = gender
        )

        info = {
            "submitted": True,
            "firstname": firstname,
            "lastname": lastname,
            "age": age,
            "gender": gender,
        }

        return render(request, "cms.html", info)

    return render(request, "cms.html")
