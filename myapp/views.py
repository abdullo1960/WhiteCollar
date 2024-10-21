from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import (Info, Contact, BlogModel, 
                     MessageModel, Testimonial, ExpertsModel,
                     DataModel, EmailModel, LocationModel)

def homePageView(request):
    objects = Info.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        year = request.POST.get("year")
        hour = request.POST.get("hour")
        text = request.POST.get("text")
        if not phone_number:
            phone_number = None
        if not year:
            year = None
        Contact.objects.create(name=name, email=email, phone_number=phone_number, year=year, hour=hour, text=text)
        messages.info(request, "Xabar qabul qilindi")
    testimonials = Testimonial.objects.all()
    datas = DataModel.objects.all()
    emails = EmailModel.objects.all()
    locations = LocationModel.objects.all()
    context = {
    "objects": objects,
    "testimonials": testimonials,
    "datas": datas,
    "emails": emails,
    "locations": locations
    }
    return render(request, 'home.html', context)

def aboutPageView(request):
    teams = ExpertsModel.objects.all()
    datas = DataModel.objects.all()
    emails = EmailModel.objects.all()
    locations = LocationModel.objects.all()
    email = request.POST.get("email")
    Contact.objects.create(email=email)
    messages.info(request, "Xabar qabul qilindi")
    context = {
    "teams": teams,
    "datas": datas,
    "emails": emails,
    "locations": locations
    }
    return render(request, "about.html", context)

def blogPageView(request):
    email = request.POST.get("email")
    Contact.objects.create(email=email)
    messages.info(request, "Xabar qabul qilindi")
    blogs = BlogModel .objects.all()
    datas = DataModel.objects.all()
    emails = EmailModel.objects.all()
    locations = LocationModel.objects.all()
    context = {
    "blogs": blogs,
    "datas": datas,
    "emails": emails,
    "locations": locations
    }
    return render(request, "blog.html", context)

def contactPageView(request):
    email = request.POST.get("email")
    Contact.objects.create(email=email)
    messages.info(request, "Xabar qabul qilindi")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        subject = request.POST.get("subject")
        text = request.POST.get("text")
        if not subject:
            subject = None
        MessageModel.objects.create(name=name, email=email, phone_number=phone_number, subject=subject, text=text)
    datas = DataModel.objects.all()
    emails = EmailModel.objects.all()
    locations = LocationModel.objects.all()
    context = {
    "datas": datas,
    "emails": emails,
    "locations": locations
    }
    return render(request, "contact.html", context)

def pricePageView(request):
    email = request.POST.get("email")
    Contact.objects.create(email=email)
    messages.info(request, "Xabar qabul qilindi")
    datas = DataModel.objects.all()
    emails = EmailModel.objects.all()
    locations = LocationModel.objects.all()
    context = {
    "datas": datas,
    "emails": emails,
    "locations": locations
    }
    return render(request, "price.html", context)

def add_servicesPageView(request):
    email = request.POST.get("email")
    Contact.objects.create(email=email)
    messages.info(request, "Xabar qabul qilindi")
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     description = request.POST.get('description')
    #     objects_with_images = Info.objects.all()
    #     if name and description and objects_with_images:
    #         Info.objects.create(name=name, description=description, objects_with_images=objects_with_images)
    
    
    objects = Info.objects.all()
    testimonials = Testimonial.objects.all()
    datas = DataModel.objects.all()
    emails = EmailModel.objects.all()
    locations = LocationModel.objects.all()
    context = {
    "objects": objects,
    "testimonials": testimonials,
    "datas": datas,
    "emails": emails,
    "locations": locations
    }
    return render(request, 'our_services.html', context)