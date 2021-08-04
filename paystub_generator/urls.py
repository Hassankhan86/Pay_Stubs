from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'paystub_generator'

urlpatterns = [

    path('homepage', views.homepage, name='homepage'),
    path('create_your_stub',views.create_your_stub, name='create_your_stub'),
    path('FAQ', views.faq, name='faq'),
    path('Stub_Samples/', views.stub_samples, name='stub_samples'),
    path('About us/', views.about_us, name='about_us'),

    path('base/', views.base, name='base')


]
