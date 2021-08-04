from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'W2_form'

urlpatterns = [

    path('w2_form_generator', views.w2_form_generator, name='w2_form_generator'),
    path('w2_form', views.w2_form, name='w2_form')
]
