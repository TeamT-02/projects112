from django.urls import path
from . import views
from rus.viewss import index_ru, about_ru, product_ru, product_detail_ru, contacts_ru, certificate_ru, \
    certificate_detail_ru



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('product', views.product, name='product'),
    path('product_detail/<str:id>/', views.product_detail, name='product_detail'),
    path('contact', views.contacts, name='contact'),
    path('certificate', views.certificate, name='certificate'),
    path('certificate_detail/<str:id>/', views.certificate_detail, name='certificate_detail'),

    # rus
    path('ru', index_ru, name='index_ru'),
    path('about/ru', about_ru, name='about_ru'),
    path('product/ru', product_ru, name='product_ru'),
    path('product_detail/<str:id>/ru', product_detail_ru, name='product_detail_ru'),
    path('contact/ru', contacts_ru, name='contact_ru'),
    path('certificate/ru', certificate_ru, name='certificate_ru'),
    path('certificate_detail/<str:id>/ru', certificate_detail_ru, name='certificate_detail_ru'),
]
