from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from eng.models import *
from .forms import ContactForm
from django.http import HttpResponse


def index(request):
    slider = Home_slider.objects.order_by('-id')[:3]
    about = Home_about.objects.order_by('-id')[:1]
    services = Home_Services.objects.order_by('-id')[:6]
    video_link = Home_video.objects.order_by('-id')[:1]
    home_projects_about = Home_project_about.objects.order_by('-id')[:1]
    home_projects = Home_project.objects.order_by('-id')[:6]
    testimonials = Testimonials.objects.order_by('-id')[:6]
    if request.method == "POST":
        contact = Home_Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.save()
    ctx = {
        'slider': slider,
        'about': about,
        'services': services,
        'video_link': video_link,
        'home_projects': home_projects,
        'home_projects_about': home_projects_about,
        'testimonials': testimonials
    }
    return render(request, 'en/index.html', ctx)


def about(request):
    abouts = Home_about.objects.order_by('-id')[:1]
    big_about = Big_About.objects.order_by('-id')[:1]
    results = Results.objects.order_by('-id')[:4]
    testimonials = Testimonials.objects.order_by('-id')[:6]
    context = {
        'abouts': abouts,
        'big_about': big_about,
        'results': results,
        'testimonials': testimonials
    }
    return render(request, 'en/about-us.html', context)


def product(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'en/products.html', context)


def product_detail(request, id):
    product = Products.objects.filter(id=id).first()
    context = {
        'product': product
    }
    return render(request, 'en/product-details.html', context)


def contacts(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        messages = request.POST.get('messages')

        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.subject = subject
        contact.messages = messages
        contact.save()
    return render(request, 'en/contact.html')


def certificate(request):
    products = Certificate.objects.all()
    context = {
        'products': products
    }
    return render(request, 'en/products_sertificat.html', context)


def certificate_detail(request, id):
    certificate = Certificate.objects.filter(id=id).first()
    context = {
        'certificate': certificate
    }
    return render(request, 'en/products_sertificat_details.html', context)
