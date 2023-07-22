from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.contrib.auth.models import User, AbstractUser


class Home_slider(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    img = models.ImageField(upload_to='images/img/slider/')
    number_id = models.IntegerField()


# class CustomUser(AbstractUser):
#     about = models.TextField(max_length=300)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     # user_type = models.CharField(choices=USER, max_length=50, default=1)
#     profile_pic = models.ImageField(upload_to='media/profile_pic')


class Home_about(models.Model):
    images_one = models.ImageField(upload_to='images/img/about/')
    # images_two = models.ImageField(upload_to='images/img/about/')
    title = models.CharField(max_length=45)
    text = models.TextField()


class Home_Services(models.Model):
    images = models.ImageField(upload_to='images/img/services/')
    title = models.CharField(max_length=30)
    text = models.TextField()


class Home_video(models.Model):
    video_link = models.CharField(max_length=250)


class Home_project_about(models.Model):
    images_one = models.ImageField(upload_to='images/img/project/one/')
    images_two = models.ImageField(upload_to='images/img/project/two/')
    title = models.CharField(max_length=55)
    text = models.TextField()


class Home_project(models.Model):
    images = models.ImageField(upload_to='images/img/project/')
    title = models.CharField(max_length=30)


class Testimonials(models.Model):
    text = models.TextField()
    full_name = models.CharField(max_length=60)
    jobs_name = models.CharField(max_length=40)


class Big_About(models.Model):
    title = models.CharField(max_length=40)
    images_one = models.ImageField(upload_to='images/img/about_us/one/')
    images_two = models.ImageField(upload_to='images/img/about_us/two/')
    text = models.TextField()


class Results(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()


class Home_Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.TextField()


class Products(models.Model):
    product_images = models.ImageField(upload_to='images/product/img/')
    title = models.CharField(max_length=46)
    price = models.IntegerField()
    text = models.TextField()
    phone_numbers = models.CharField(max_length=250, default=+998 - 99 - 125 - 55 - 44)


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=60)
    subject = models.CharField(max_length=150)
    text = models.TextField()


class Certificate(models.Model):
    img = models.ImageField(upload_to='images/img/Certificate/')
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    about = models.TextField()