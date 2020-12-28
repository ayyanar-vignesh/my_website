from django.shortcuts import render
from django.http import HttpResponse
from sub_part.models import Contact


# Create your views here.

def index(request):
    return render(request, "sub_part/index.html")


def about(request):
    dic1 = {"name": "inr", "college": "loyola college"}

    return render(request, "sub_part/about.html", dic1)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name,email,phone,desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("The data has been written to the db")

    return render(request, "sub_part/contact.html")


def projects(request):
    return render(request, "sub_part/projects.html")